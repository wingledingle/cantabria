# Iowa Lead Watch

An unofficial, single-page tracker for the Army's planned lead azide detonation at the Iowa Army
Ammunition Plant (Middletown, Iowa), built on the open model and saved forecasts of the
[Iowa Lead Tracker](https://github.com/iowaleadtracker/iowaleadtracker) (iowaleadtracker.com)
plus Army, FEMA, EPA, state and news sources (listed on the page).

What it shows:
- countdown to the scheduled time (9:00 a.m. CST, Nov. 25, 2026) and status
- hour-by-hour wind at the plant from four models (HRRR, RRFS, GFS, ECMWF), checked against the EPA
  emergency permit's limits (surface wind 1–15 mph, ≤30 mph at 1,000–3,000 ft, no rain)
- a downwind dial: towns by direction and distance, with the sector the cloud heads toward out to
  the tracker's modeled ground-lead reach for each release case
- reach of each EPA dust-lead level and peak air concentration per release case
- official guidance, a timeline, the tracker's latest commits, and sources

## Run

Any static host works: serve this folder (`python3 -m http.server`) and open `index.html`.
On a normal web host the page refreshes weather from Open-Meteo and commits from the GitHub API
every 10 minutes; when those are blocked it uses `snapshot.js`.

## Refresh the snapshot

```bash
git clone --depth 60 https://github.com/iowaleadtracker/iowaleadtracker /tmp/ilt
python3 tools/snapshot.py /tmp/ilt > snapshot.js
```

Release-case numbers, the timeline and `STATUS_ASOF` are written in `index.html`; update them by hand
from the tracker's `llms.txt` and official sources.

Not affiliated with the Iowa Lead Tracker, the Army or any agency. Don't use it to decide whether
you're safe; follow local officials.
