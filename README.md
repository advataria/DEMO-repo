** DEMO-repo
Demo repository, private repository available upon request

# Advataria Demo – Autonomous Creative Pipeline (Public Version)

This repository contains a **simplified public demo** of the Advataria creative pipeline.  
It demonstrates the structure and JSON outputs of our three core agents:

1. **AdvaScout (demo)** – Extracts a structured brand snapshot from a URL (or offline mode).  
2. **AdvaBrief (demo)** – Converts the Scout JSON into a creative brief.  
3. **AdvaStory (demo)** – Generates a 5-scene storyboard from the brief.

> ⚠️ This demo does **not** include proprietary logic, LLM prompt engineering, Gemini/Veo integrations, or production agent code.  
> It contains only safe, non-sensitive demo logic.

The full production repository (private) is accessible to the Fetch Grant Technical Review Team upon request.

---

##  Quick Start (CLI Demo)

### 1) AdvaScout Demo

bash
python cli_demo/advascout_demo.py \
    --url https://procare.sk \
    --notes "Client wants conversions" \
    --out examples/scout_demo.json
Offline mode:

bash
Copy code
python cli_demo/advascout_demo.py \
    --url https://demo-url.com \
    --offline \
    --out examples/scout_offline.json
2) AdvaBrief Demo
bash
Copy code
python cli_demo/advabrief_demo.py \
    --input examples/scout_example_procare.json \
    --out examples/brief_demo.json
3) AdvaStory Demo
bash
Copy code
python cli_demo/advastory_demo.py \
    --input examples/brief_example_procare.json \
    --out examples/story_demo.json
    
Example Outputs
Sample structured outputs are provided in:

pgsql
Copy code
examples/
  scout_example_procare.json
  brief_example_procare.json
  story_example_procare.json
These show the expected JSON schemas used by the real Advataria pipeline.

🧩 Architecture (Demo Version)
pgsql
Copy code
URL / notes
   │
   ▼
[AdvaScout demo]  → (JSON) →  [AdvaBrief demo]  → (JSON) →  [AdvaStory demo]
        │                         │                        │
    scout.json               brief.json               story.json
The real system mirrors this pipeline with production-grade agents, LLM logic and uAgents orchestration.

For more detail, see ARCHITECTURE.md.

🔒 Full Production Codebase (Private)
The private production repository contains:

multi-agent orchestration,

AI-powered brief, story & storyboard engines,

data acquisition agent,

Gemini / Veo / Sora integrations,

backend API & frontend UI.

It is available for read-only review by the Fetch.ai Grant Technical Review Team.

📄 License
All rights reserved.
This repository is a demonstration-only subset of the Advataria system and does not grant any rights to the proprietary production implementation.**
