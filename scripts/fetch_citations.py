"""Fetch the Google Scholar citation count and write it to citations.json.

Run daily by .github/workflows/scholar-citations.yml. Google blocks automated
requests from datacenter IPs fairly often, so a failed fetch is not an error:
the script leaves the existing citations.json untouched and exits 0, and the
site keeps showing the last good number.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

SCHOLAR_ID = "5dfoO-AAAAAJ"
OUTPUT = Path(__file__).resolve().parent.parent / "citations.json"
PROFILE_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)


def log(message):
    print(message)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(message + "\n")


def via_scholarly():
    from scholarly import scholarly

    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=["indices"])
    return int(author["citedby"])


def via_profile_page():
    """Fallback: parse the citation total straight off the profile page."""
    request = urllib.request.Request(PROFILE_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")
    totals = re.findall(r'gsc_rsb_std">(\d+)<', html)
    if not totals:
        raise ValueError("no citation totals found in profile page")
    return int(totals[0])


def main():
    citations = None
    for source in (via_scholarly, via_profile_page):
        try:
            citations = source()
            log(f"Fetched {citations} citations via {source.__name__}.")
            break
        except Exception as error:  # noqa: BLE001 - any failure means try the next source
            log(f"{source.__name__} failed: {error}")

    if citations is None:
        log("No source succeeded. Keeping the existing count.")
        return 0

    previous = None
    if OUTPUT.exists():
        previous = json.loads(OUTPUT.read_text(encoding="utf-8")).get("citations")

    if previous is not None and citations < previous:
        log(f"Refusing to lower the count from {previous} to {citations}.")
        return 0

    OUTPUT.write_text(
        json.dumps({"citations": citations, "updated": date.today().isoformat()}, indent=2) + "\n",
        encoding="utf-8",
    )
    log(f"Wrote {citations} citations to {OUTPUT.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
