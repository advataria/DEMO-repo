#!/usr/bin/env python
"""
AdvaStory Demo – Brief JSON -> 5-scene Storyboard (JSON)

Usage:
  python cli_demo/advastory_demo.py --input examples/brief_example_procare.json --out examples/story_demo_output.json
"""

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List


@dataclass
class Scene:
    id: int
    timestamp: str
    visual: str
    voiceover: str
    on_screen_text: str
    notes: str


@dataclass
class StoryResult:
    format: str
    duration_seconds: int
    platform_hint: str
    scenes: List[Scene]
    final_frame: Dict[str, Any]


def demo_story_from_brief(brief: Dict[str, Any]) -> StoryResult:
    campaign_title = brief.get("campaign_title", "Brand Campaign")
    brand_name = campaign_title.split(":")[0] if ":" in campaign_title else campaign_title
    cta = brief.get("cta", "Get started")
    target_audience = brief.get("target_audience", "your audience")
    smp = brief.get("single_minded_proposition", "Your simple key message.")
    tone = brief.get("tone_of_voice", "Friendly and clear")
    channels = brief.get("channels", ["TikTok", "Instagram Reels", "YouTube Shorts"])
    duration_seconds = brief.get("duration_seconds", 30)

    format_ = "9:16 vertical"
    platform_hint = ", ".join(channels)

    scenes: List[Scene] = []

    # Scene 1 – Hook
    scenes.append(
        Scene(
            id=1,
            timestamp="0–3s",
            visual=f"Fast, attention-grabbing shot of a problem {target_audience} faces.",
            voiceover="Still struggling with the same problem every day?",
            on_screen_text="Stop wasting time.",
            notes="Use bold typography, dynamic movement, and a quick sound cue.",
        )
    )

    # Scene 2 – Problem / tension
    scenes.append(
        Scene(
            id=2,
            timestamp="3–8s",
            visual="Quick montage of people in real-life situations, looking frustrated.",
            voiceover=f\"\"\"You're not alone. Many {target_audience} feel exactly the same.\"\"\"",
            on_screen_text="You’re not alone.",
            notes="Keep cuts short, show emotion and relatability.",
        )
    )

    # Scene 3 – Solution
    scenes.append(
        Scene(
            id=3,
            timestamp="8–15s",
            visual=f"Smooth transition to a clean interface or scene introducing {brand_name}.",
            voiceover=f\"\"\"That's why {brand_name} exists – {smp.lower()}\"\"\"",
            on_screen_text=f"{brand_name} makes it simple.",
            notes="Show product/service in action with clear visuals.",
        )
    )

    # Scene 4 – Benefits
    scenes.append(
        Scene(
            id=4,
            timestamp="15–23s",
            visual="3–4 quick shots: before/after, dashboard with improved results, relaxed user.",
            voiceover="In just a short time, you see the difference: more clarity, less stress, and real results.",
            on_screen_text="More clarity. Less stress. Real results.",
            notes="Overlay simple icons or stats. Ensure readability on mobile screens.",
        )
    )

    # Scene 5 – CTA
    scenes.append(
        Scene(
            id=5,
            timestamp="23–30s",
            visual=f"Hero frame with {brand_name} logo, short tagline, and a clear CTA button.",
            voiceover=f\"\"\"Join others who already switched. {cta}.\"\"\"",
            on_screen_text=cta,
            notes="Freeze the last 2 seconds so the logo and CTA are easy to read.",
        )
    )

    final_frame = {
        "visual": f"{brand_name} logo centered, CTA button below, short tagline above.",
        "tagline": smp,
        "cta": cta,
        "notes": "This is the frame that users see when they pause or end the video.",
    }

    return StoryResult(
        format=format_,
        duration_seconds=duration_seconds,
        platform_hint=platform_hint,
        scenes=scenes,
        final_frame=final_frame,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Advataria – AdvaStory Demo CLI")
    parser.add_argument("--input", required=True, help="Input Brief JSON file.")
    parser.add_argument("--out", default=None, help="Output Story JSON file.")
    args = parser.parse_args()

    input_path = Path(args.input)
    brief_data = json.loads(input_path.read_text(encoding="utf-8"))

    result = demo_story_from_brief(brief_data)
    payload = json.dumps(asdict(result), indent=2, ensure_ascii=False)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload, encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
