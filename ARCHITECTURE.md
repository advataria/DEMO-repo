# Advataria Demo – Architecture

This document describes the architecture of the **public demo pipeline** contained in this repository.  
It is a simplified version of the real Advataria system and is designed only for safe, non-proprietary evaluation.

---

## 1. High-Level Overview

The demo pipeline consists of three sequential CLI agents:

1. **AdvaScout (demo)**  
   - Input: URL (and optional client notes)  
   - Output: structured brand snapshot JSON  

2. **AdvaBrief (demo)**  
   - Input: AdvaScout JSON  
   - Output: structured creative brief JSON  

3. **AdvaStory (demo)**  
   - Input: AdvaBrief JSON  
   - Output: 5-scene storyboard JSON  

Data flow:

URL / notes
   │
   ▼
[AdvaScout demo]  →  scout.json  →  [AdvaBrief demo]  →  brief.json  →  [AdvaStory demo]  →  story.json

Each step is stateless and communicates via JSON files.  
This mirrors the structure of the production system, where each step is implemented as an agent with a clear I/O contract.

---

## 2. Components

### 2.1 AdvaScout (demo)

Responsibility:  
Extracts a structured description of a brand from:
- a real URL (if HTTP is available), or  
- a fixed offline demo mode (no network), for safe reproducibility.

Key tasks:
- fetch URL (if not in offline mode),
- extract simple metadata (title, description),
- apply basic heuristics to guess offers, audience, tone,
- build a normalized JSON snapshot.

---

### 2.2 AdvaBrief (demo)

Responsibility:  
Transform the Scout JSON into a performance-focused creative brief.

Key tasks:
- derive campaign title, objective, KPIs, SMP,
- suggest tone, channels, CTA,
- output structured JSON.

---

### 2.3 AdvaStory (demo)

Responsibility:  
Generate a structured 5-scene storyboard from the brief.

Key tasks:
- construct scenes with timestamps, visuals, text and voiceover,
- define a final CTA frame,
- output storyboard JSON.

---

## 3. JSON Schemas (Demo)

### 3.1 AdvaScout Demo JSON

{
  "brand_name": "string",
  "website_url": "string",
  "tagline": "string",
  "summary": "string",
  "offers": ["string"],
  "target_audience": "string",
  "tone_of_voice": "string",
  "key_messages": ["string"],
  "proof_points": ["string"],
  "competitors": ["string"],
  "raw_source_excerpt": "string"
}

---

### 3.2 AdvaBrief Demo JSON

{
  "campaign_title": "string",
  "primary_objective": "string",
  "kpi": ["string"],
  "target_audience": "string",
  "single_minded_proposition": "string",
  "tone_of_voice": "string",
  "channels": ["string"],
  "cta": "string",
  "duration_seconds": 30,
  "mandatories": ["string"],
  "references": ["string"]
}

---

### 3.3 AdvaStory Demo JSON

{
  "format": "string",
  "duration_seconds": 30,
  "platform_hint": "string",
  "scenes": 
    {
      "id": 1,
      "timestamp": "string",
      "visual": "string",
      "voiceover": "string",
      "on_screen_text": "string",
      "notes": "string"
    }
  ],
  "final_frame": {
    "visual": "string",
    "tagline": "string",
    "cta": "string",
    "notes": "string"
  }
}

---

## 4. Relation to the Production Advataria System

The real Advataria system extends this demo with:
- LLM-based Scout/Brief/Story agents (Gemini, Veo, Sora),
- multi-agent orchestration,
- prompt engineering, refinement loops,
- Fetch/uAgents integration for decentralized execution.

This demo exposes only the data contracts and safe rule-based logic.

---

## 5. Intended Fetch/uAgents Mapping

Scout uAgent  
Brief uAgent  
Story uAgent  
Orchestrator uAgent

Each uAgent exchanges JSON messages and can issue execution receipts.

---

## 6. Limitations of the Demo

- No proprietary logic or prompts  
- No LLM calls  
- No production UI/backend  
- No agent orchestration  

This demo is intended for evaluation only.
