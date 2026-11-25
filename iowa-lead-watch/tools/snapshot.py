"""Build snapshot.js for Iowa Lead Watch from a clone of iowaleadtracker/iowaleadtracker.

Usage: python3 tools/snapshot.py /path/to/iowaleadtracker  > snapshot.js
Reads the tracker's saved Open-Meteo forecasts (met_cache/map_met_all.json) and its git log.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

MPH = 2.23694
CST = timezone(timedelta(hours=-6))
LEVELS = [1000, 975, 950, 925, 900, 850, 800, 700]
ALOFT_FT = (1000, 3000)
NAMES = {"ncep_hrrr_conus": "HRRR", "ncep_rrfs_conus": "RRFS", "gfs_global": "GFS", "ecmwf_ifs025": "ECMWF"}


def main() -> None:
    root = Path(sys.argv[1])
    met = json.loads((root / "scenarios/iowa-aap-lead-azide/met_cache/map_met_all.json").read_text())
    fetched = met["__fetched__"]
    out: dict = {"models": {}}
    pulled = []
    for url, data in met.items():
        if url == "__fetched__" or "end_date=2026-11-26" not in url:
            continue
        model = url.split("models=")[1].split("&")[0]
        if model not in NAMES:
            continue
        if "latitude=40.8255&" in url:  # single point at the plant: surface fields
            h = data["hourly"]
            m = out["models"].setdefault(NAMES[model], {})
            m["elev"] = data.get("elevation", 222)
            m["t"] = [datetime.fromisoformat(t).replace(tzinfo=timezone.utc).isoformat() for t in h["time"]]
            m["ws10"] = [None if v is None else round(v * MPH, 1) for v in h["wind_speed_10m"]]
            m["wd10"] = h["wind_direction_10m"]
            m["cloud"] = h["cloud_cover"]
            m["precip"] = h["precipitation"]
            m["temp"] = h["temperature_2m"]
            pulled.append(fetched[url])
        elif "hPa" in url:  # 5x5 grid; the centre (index 12) is the plant
            c = data[12]["hourly"]
            m = out["models"].setdefault(NAMES[model], {})
            elev = data[12].get("elevation", 222)
            aloft = []
            for i in range(len(c["time"])):
                best = None
                for lv in LEVELS:
                    z, s = c.get(f"geopotential_height_{lv}hPa"), c.get(f"wind_speed_{lv}hPa")
                    if not z or not s or z[i] is None or s[i] is None:
                        continue
                    agl_ft = (z[i] - elev) / 0.3048
                    if ALOFT_FT[0] <= agl_ft <= ALOFT_FT[1]:
                        best = max(best or 0, s[i] * MPH)
                aloft.append(None if best is None else round(best, 1))
            m["aloft"] = aloft
    out["pulled"] = max(pulled)
    log = subprocess.run(
        ["git", "-C", str(root), "log", "-25", "--format=%cI%x1f%h%x1f%s"],
        capture_output=True, text=True, check=True,
    ).stdout.strip().splitlines()
    out["commits"] = [dict(zip(("date", "sha", "msg"), line.split("\x1f"))) for line in log]
    out["built"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print("window.SNAPSHOT = " + json.dumps(out, separators=(",", ":")) + ";")


if __name__ == "__main__":
    main()
