import feedparser
from ..models import Job
from ..utils import clean_text, keyword_match, stable_id

FEEDS = [
    "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-back-end-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-front-end-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss",
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
                platform="We Work Remotely", title=title, company=clean_text(entry.get("author")),
                location="Remote", url=url, apply_url=url, description=desc,
                published_at=entry.get("published",""),
                tags=[],
                source_id=stable_id("We Work Remotely", url, title, entry.get("author",""))
            ))
    return jobs
