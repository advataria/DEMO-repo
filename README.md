# DEMO-repo
Demo repository, private repository available upon request

# Advataria Demo – Scout → Brief → Story (CLI)

This repository contains a **simplified public demo** of the Advataria pipeline.

It showcases the core idea of our autonomous creative agents:

1. **AdvaScout (demo)** – extracts a structured brand snapshot from a URL (or dummy text).
2. **AdvaBrief (demo)** – turns the Scout JSON into a creative brief.
3. **AdvaStory (demo)** – generates a 5-scene storyboard from the brief.

> ⚠️ This is a **non-proprietary, simplified version** of the internal Advataria agents.  
> No proprietary prompt logic, ML models or production code are included.

The full production codebase (backend, frontend, Gemini/VEO integrations, orchestrator) is kept in a **private repository** and can be shared with the Fetch Grant Technical Review team under private access.

---

## Quick Start

bash
git clone https://github.com/<your-org>/advataria-demo.git
cd advataria-demo
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt   # (optional, if you decide to add one)
