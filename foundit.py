import requests
from bs4 import BeautifulSoup
from ..models import Job
from ..utils import clean_text, keyword_match, stable_id

SEARCH_URL = "https://www.foundit.in/srp/results"

def fetch(keywords, location="India", timeout=20):
    # Discovery only. Respect the site's robots.txt and terms before enabling.
    q = " ".join(keywords[:4])
    r = requests.get(
        SEARCH_URL,
        params={"query": q, "location": location},
        headers={"User-Agent": "job-agent/1.0"},
        timeout=timeout,
    )
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    jobs = []
    for card in soup.select("div.jobCard, div[data-testid='job-card']"):
        title_el = card.select_one("h3, a")
        if not title_el:
            continue
        title = clean_text(title_el.get_text(" ", strip=True))
        link = title_el.get("href", "") if title_el.name == "a" else ""
        if link.startswith("/"):
            link = "https://www.foundit.in" + link
        if not keyword_match(title, clean_text(card.get_text(" ", strip=True)), keywords, ["sales","marketing","legal"]):
            continue
        jobs.append(Job(
            platform="Foundit", title=title, location=location,
            url=link or SEARCH_URL, apply_url=link or SEARCH_URL,
            description=clean_text(card.get_text(" ", strip=True)),
            source_id=stable_id("Foundit", link, title, "")
        ))
    return jobs
