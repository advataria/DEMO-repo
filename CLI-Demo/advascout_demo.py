#!/usr/bin/env python
"""
AdvaScout Demo – URL -> Structured Brand Snapshot (JSON)

Usage:
  python cli_demo/advascout_demo.py --url https://procare.sk --out examples/scout_demo.json
  python cli_demo/advascout_demo.py --url https://example.com --offline --out examples/scout_offline.json
"""

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional

try:
    import requests
except ImportError:
    requests = None


@dataclass
class ScoutResult:
    brand_name: str
    website_url: str
    tagline: str
    summary: str
    offers: List[str]
    target_audience: str
    tone_of_voice: str
    key_messages: List[str]
    proof_points: List[str]
    competitors: List[str]
    raw_source_excerpt: str


def simple_clean_text(html: str) -> str:
    html = re.sub(r"<script.*?>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style.*?>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        return ""
    title = m.group(1).strip()
    title = re.split(r"[\|\-\–•]", title)[0].strip()
    return title


def extract_meta_description(html: str) -> str:
    m = re.search(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if m:
        return m.group(1).strip()
    m = re.search(
        r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if m:
        return m.group(1).strip()
    return ""


def demo_scout_from_url(url: str, notes: Optional[str] = None, offline: bool = False) -> ScoutResult:
    """
    Simplified demo logic:
    - If offline=True or requests is unavailable, returns a hard-coded example.
    - Otherwise, fetches the URL and applies simple heuristics.
    """
    if offline or requests is None:
        brand_name = "Demo Brand"
        text_excerpt = "This is an offline demo. No live HTTP request was performed."
        tagline = "Demo Brand – demo tagline for illustration."
        summary = "Demo summary of the brand based on offline mode."
        offers = ["Demo product A", "Demo service B"]
        if notes:
            offers.append(f"Client notes: {notes}")
        target_audience = "Demo target audience"
        tone = "Friendly, simple, explanatory"
        key_messages = [
            "Demo Brand provides a simple example.",
            "This output is suitable for demonstrating the JSON structure."
        ]
        proof_points = ["Demo-only data."]
        competitors = ["Demo Competitor 1", "Demo Competitor 2"]
        return ScoutResult(
            brand_name=brand_name,
            website_url=url,
            tagline=tagline,
            summary=summary,
            offers=offers,
            target_audience=target_audience,
            tone_of_voice=tone,
            key_messages=key_messages,
            proof_points=proof_points,
            competitors=competitors,
            raw_source_excerpt=text_excerpt,
        )

    # Live HTTP mode
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    html = resp.text

    title = extract_title(html)
    meta_desc = extract_meta_description(html)
    cleaned = simple_clean_text(html)

    text_excerpt = cleaned[:500]
    brand_name = title or url.replace("https://", "").replace("http://", "").split("/")[0]

    if meta_desc:
        tagline = meta_desc[:160] + ("..." if len(meta_desc) > 160 else "")
        summary = meta_desc
    else:
        tagline = f"{brand_name} – online presence"
        summary = f"Automatic summary placeholder for {brand_name}."

    offers: List[str] = []
    lower_text = (meta_desc + " " + cleaned).lower()

    if "clinic" in lower_text or "hospital" in lower_text or "doctor" in lower_text:
        offers.append("Healthcare services and medical consultations")
        target_audience = "Patients seeking medical care and preventive check-ups"
    elif "software" in lower_text or "saas" in lower_text:
        offers.append("Software-as-a-service product")
        target_audience = "Businesses looking for a digital software solution"
    elif "shop" in lower_text or "store" in lower_text or "e-commerce" in lower_text:
        offers.append("Online shopping / e-commerce products")
        target_audience = "Consumers purchasing products online"
    else:
        offers.append("Main products or services described on the website")
        target_audience = "Target customers of the brand (to be refined)."

    if notes:
        offers.append(f"Client notes: {notes}")

    if "luxury" in lower_text or "premium" in lower_text:
        tone = "Premium, aspirational, elegant"
    elif "fast" in lower_text or "simple" in lower_text or "easy" in lower_text:
        tone = "Simple, friendly, accessible"
    else:
        tone = "Professional, trustworthy, informative"

    key_messages = [
        f"{brand_name} provides: {offers[0]}",
        "Focus on quality and customer satisfaction.",
    ]
    proof_points = [
        "Website highlights expertise, experience or track record (to be refined).",
        "Modern, user-friendly presentation (from demo heuristics).",
    ]
    competitors = [
        "Top 2–3 competitors in the same category (to be researched in a full version)."
    ]

    return ScoutResult(
        brand_name=brand_name,
        website_url=url,
        tagline=tagline,
        summary=summary,
        offers=offers,
        target_audience=target_audience,
        tone_of_voice=tone,
        key_messages=key_messages,
        proof_points=proof_points,
        competitors=competitors,
        raw_source_excerpt=text_excerpt,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Advataria – AdvaScout Demo CLI")
    parser.add_argument("--url", required=True, help="Website URL of the brand.")
    parser.add_argument("--notes", default=None, help="Optional client notes.")
    parser.add_argument("--out", default=None, help="Output JSON file path.")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Use offline demo mode (no HTTP request, fixed demo data).",
    )
    args = parser.parse_args()

    result = demo_scout_from_url(url=args.url, notes=args.notes, offline=args.offline)
    data = asdict(result)
    payload = json.dumps(data, indent=2, ensure_ascii=False)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload, encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
