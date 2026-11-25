# Cantabria — Dingo Butler Assistant

## Original request (source of truth)

Build a **working, fully animated 2D pixel-art dingo butler assistant**, faithfully based on the user's supplied reference image and supplied GLB model. It should be a polished Clippy-like assistant that lives on Android first, with Windows and Linux versions later.

This is **not** a request for a static illustration, a looping GIF, a rough prototype, or a minimally animated mascot. The user specifically insists on excellent animation quality, detailed rigging, a great visual appearance, and a **working Android assistant**. Do not substitute a half-finished sample app for the finished product.

The assistant must let the user converse through the character using **ChatGPT (OpenAI), Claude (Anthropic), or Mistral**. Conversation should drive expressive, contextually appropriate character animations; it should be capable of speaking its responses aloud and reacting naturally to user input.

The supplied **image is the definitive visual reference**: a small friendly orange/golden dingo with huge upright ears, white/cream muzzle, cheek fur, expressive eyes and eyebrows, tail, white shirt, black/dark suit and bow tie, and little paw pads. Translate the character into **high-quality 2D pixel art**, preserving its recognizable design and butler personality. The accompanying GLB is a supplementary source/reference, not permission to switch to a 3D character in the finished app.

### Required deliverables
- Installable, usable **Android APK**, with source code and reproducible build instructions.
- A polished **fully articulated 2D pixel-art character rig** with independent head, eyes, eyelids, pupils, eyebrows, ears, muzzle, jaw/mouth, neck, torso, shoulders, arms, paws and digits where warranted, hips, legs, feet, and tail; avoid detached, sliding, or visually broken limbs.
- Detailed, meticulously drawn pixel-art animation frames and seamless transitions, not cheap transforms or simple idle loops. Preserve crisp pixel edges at every screen scale. Combine animation rigging with hand-drawn frames where this produces better results.
- At least **40 distinct, production-quality animation sequences** with variations and transitions across idle breathing and blinking, ear twitching, tail movement, walking, running, sitting, jumping, greeting, waving, bowing, suit/bow-tie adjustment, presenting and pointing, thinking, scratching chin, confusion, joy, concern, surprise, sadness, frustration, listening, sleeping and waking, as well as speaking.
- Convincing **speech animations/lip synchronization** (visemes/phonemes where available), eye contact, gaze, gestures, and emotion/intent-driven behavior while the AI speaks; robust interruption and listening/speaking/thinking state handling.
- **Android floating overlay** (where permissions allow), movable/dragging character, touch interactions, conversation UI, microphone input, text chat, speech-to-text, text-to-speech, provider/model selection, configurable voice and settings.
- Support **ChatGPT/OpenAI, Claude, and Mistral** as conversation backends; clearly distinguish official API integrations from subscription app interfaces. Do not falsely claim a ChatGPT or Claude consumer subscription includes API access or invent free API methods. Offer practical, lawful alternatives where subscriptions cannot directly power third-party apps.
- **No required ongoing paid service**; user already pays for GPT and Claude subscriptions and does not want to pay anyone else. Prefer free local/offline features, freely available tools, and commercially usable assets; disclose any genuine integration limitations rather than hiding them.
- Modular architecture so the Android character, behavior system, and provider adapters can later support **Windows and Linux** without redoing the artwork.
- Test animation quality, rig layering and pivots, overlays, permissions, lifecycle, performance, and actual conversational behavior on Android. No placeholders, incomplete demos or fake functionality presented as completed features.

### Priorities and acceptance tests
1. Looks unmistakably like the reference dingo, in exceptionally detailed and consistent pixel art.
2. Character feels *alive*: smooth, expressive full-body animation and proper lip-sync tied to live conversation.
3. Actually works as an Android voice/text assistant with the stated provider options and accessible fallback paths.
4. No mandatory recurring fees; build/output rights suitable for the user's intended commercial use.
5. Windows and Linux follow **after** Android meets the quality bar.

### Supplied original files
- `assets/reference/dingo-butler-original.webp` — the user-supplied reference image (original upload was labeled `12747.jpg`, but content is WebP).
- `assets/reference/dingo-butler-original.glb` — the user-supplied 3D model (`sample_2026-11-25T024937.335.glb`), for asset/design reference.

**Explicit instruction:** The earlier assistant-generated `Dingo-Android-source.zip` is rejected by the user and **must not be imported or treated as the intended codebase**. Start from the original image, GLB, and requirements above.
