# DEMO-repo
Public demo repository. Full private repository available upon request for Fetch Grant Technical Review.

# Advataria Demo – Autonomous Creative Pipeline (Public Version)

This repository contains a simplified public demo of the Advataria creative pipeline.
It demonstrates the structure and JSON outputs of our three core agents:

1. AdvaScout (demo) – Extracts a structured brand snapshot from a URL (or offline mode).
2. AdvaBrief (demo) – Converts the Scout JSON into a creative brief.
3. AdvaStory (demo) – Generates a 5-scene storyboard from the brief.

⚠️ This demo does NOT include proprietary logic, LLM prompt engineering, Gemini/Veo integrations, or production agent code.
It contains only safe, non-sensitive demo logic.

The full production repository is private and available to the Fetch Grant Technical Review Team upon request.

---

## Quick Start (CLI Demo)

git clone https://github.com/<your-org>/advataria-demo.git
cd advataria-demo
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

---

## Run the Demo Agents (Scout → Brief → Story)

1) AdvaScout Demo

python cli_demo/advascout_demo.py \
  --url https://procare.sk \
  --notes "Client wants conversions" \
  --out examples/scout_demo.json

Offline mode (no HTTP request):

python cli_demo/advascout_demo.py \
  --url https://demo-url.com \
  --offline \
  --out examples/scout_offline.json

---

2) AdvaBrief Demo

python cli_demo/advabrief_demo.py \
  --input examples/scout_example_procare.json \
  --out examples/brief_demo.json

---

3) AdvaStory Demo

python cli_demo/advastory_demo.py \
  --input examples/brief_example_procare.json \
  --out examples/story_demo.json

---

## Example Outputs

examples/
  scout_example_procare.json
  brief_example_procare.json
  story_example_procare.json

These reflect the schemas used in the full Advataria production pipeline.

---

## Architecture (Demo Version)

URL / notes
   |
   v
[AdvaScout demo] → scout.json → [AdvaBrief demo] → brief.json → [AdvaStory demo] → story.json

See ARCHITECTURE.md for details.

---

## Full Production Codebase (Private)

Includes:
- multi-agent orchestration
- AI-powered brief & storyboard engines
- data acquisition agent
- Gemini / Veo / Sora integrations
- backend API & frontend UI

Available for read-only review to the Fetch.ai Grant Technical Review Team upon request.

---

## License

All rights reserved.
This repository is a demonstration-only subset and does not grant rights to the proprietary production implementation.
