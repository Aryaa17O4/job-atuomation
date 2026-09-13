import feedparser
from ..models import Job
from ..utils import clean_text, keyword_match, stable_id

FEEDS = [
    "https://jobspresso.co/feed/",
]

def fetch(keywords):
    jobs = []
    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = clean_text(entry.get("title"))
            desc = clean_text(entry.get("summary"))
            if not keyword_match(title, desc, keywords, ["sales", "marketing", "legal"]):
                continue
            url = entry.get("link", "")
            jobs.append(Job(
                platform="Jobspresso", title=title, company=clean_text(entry.get("author")),
                location="Remote", url=url, apply_url=url, description=desc,
                published_at=entry.get("published",""),
                source_id=stable_id("Jobspresso", url, title, entry.get("author",""))
            ))
    return jobs
