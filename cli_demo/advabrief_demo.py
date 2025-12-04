#!/usr/bin/env python
"""
AdvaBrief Demo – Scout JSON -> Creative Brief (JSON)

Usage:
  python cli_demo/advabrief_demo.py --input examples/scout_example_procare.json --out examples/brief_demo_output.json
"""

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List


@dataclass
class BriefResult:
    campaign_title: str
    primary_objective: str
    kpi: List[str]
    target_audience: str
    single_minded_proposition: str
    tone_of_voice: str
    channels: List[str]
    cta: str
    duration_seconds: int
    mandatories: List[str]
    references: List[str]


def demo_brief_from_scout(scout: Dict[str, Any]) -> BriefResult:
    brand_name = scout.get("brand_name", "The Brand")
    offers = scout.get("offers", [])
    first_offer = offers[0] if offers else "core product or service"
    target_audience = scout.get("target_audience", "primary target audience")
    tone = scout.get("tone_of_voice", "Professional and trustworthy")

    campaign_title = f"{brand_name}: Turn Attention into Action"
    primary_objective = "Performance conversions"

    kpi = [
        "Click-through rate (CTR)",
        "Cost per acquisition (CPA)",
        "Number of sign-ups / bookings / purchases",
    ]

    smp = (
        f"When you choose {brand_name}, you get {first_offer.lower()} "
        f"without the usual hassle."
    )

    channels = ["TikTok", "Instagram Reels", "YouTube Shorts"]
    cta = "Objednať sa"

    mandatories = [
        "Show brand logo in the last 2–3 seconds.",
        "Include a clear on-screen CTA.",
        "Respect brand tone of voice and visual identity.",
    ]

    references = [
        "High-performing short-form ads in this category.",
        "TikTok/Reels ads with a strong hook and clear CTA.",
    ]

    return BriefResult(
        campaign_title=campaign_title,
        primary_objective=primary_objective,
        kpi=kpi,
        target_audience=target_audience,
        single_minded_proposition=smp,
        tone_of_voice=tone,
        channels=channels,
        cta=cta,
        duration_seconds=30,
        mandatories=mandatories,
        references=references,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Advataria – AdvaBrief Demo CLI")
    parser.add_argument("--input", required=True, help="Input Scout JSON file.")
    parser.add_argument("--out", default=None, help="Output Brief JSON file.")
    args = parser.parse_args()

    input_path = Path(args.input)
    scout_data = json.loads(input_path.read_text(encoding="utf-8"))

    result = demo_brief_from_scout(scout_data)
    payload = json.dumps(asdict(result), indent=2, ensure_ascii=False)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload, encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
