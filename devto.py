import feedparser
from ..models import Job
from ..utils import clean_text, keyword_match, stable_id

def fetch(keywords, tags=("hiring",)):
    jobs = []
    for tag in tags:
        feed = feedparser.parse(f"https://dev.to/feed/tag/{tag}")
        for entry in feed.entries:
            title = clean_text(entry.get("title"))
            desc = clean_text(entry.get("summary"))
            if not keyword_match(title, desc, keywords, ["sales", "marketing", "legal"]):
                continue
            url = entry.get("link", "")
            jobs.append(Job(
                platform="DEV Community", title=title, company="",
                location="See listing", url=url, apply_url=url, description=desc,
                published_at=entry.get("published",""),
                source_id=stable_id("DEV Community", url, title, "")
            ))
    return jobs
