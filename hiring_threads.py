import feedparser
from ..models import Job
from ..utils import clean_text, keyword_match, stable_id

# HN Who's Hiring is a monthly Hacker News thread, not a conventional job API.
# This adapter is intentionally opt-in and uses the public Algolia HN API to
# discover the latest "Ask HN: Who is hiring?" thread.
ALGOLIA = "https://hn.algolia.com/api/v1/search_by_date"

def fetch(keywords, timeout=20):
    import requests
    r = requests.get(ALGOLIA, params={"query":"Ask HN: Who is hiring?", "tags":"story", "hitsPerPage":5}, timeout=timeout)
    r.raise_for_status()
    jobs = []
    for story in r.json().get("hits", []):
        # Thread-level discovery only. Individual comments require another API pass.
        title = clean_text(story.get("title"))
        url = story.get("url") or f"https://news.ycombinator.com/item?id={story.get('objectID')}"
        jobs.append(Job(
            platform="HN Who's Hiring", title=title, company="Various",
            location="See thread", url=url, apply_url=url,
            description="Monthly Hacker News hiring thread. Individual roles are in comments.",
            published_at=story.get("created_at",""),
            source_id=stable_id("HN Who's Hiring", url, title, "Various")
        ))
    return jobs
