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
