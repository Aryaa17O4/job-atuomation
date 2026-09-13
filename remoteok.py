import requests
from ..models import Job
from ..utils import clean_text, keyword_match, stable_id

URL = "https://remoteok.com/api"

def fetch(keywords, timeout=20):
    r = requests.get(URL, headers={"User-Agent": "job-agent/1.0"}, timeout=timeout)
    r.raise_for_status()
    data = r.json()
    jobs = []
    for item in data[1:]:
        title = clean_text(item.get("position"))
        desc = clean_text(item.get("description"))
        if not keyword_match(title, desc, keywords, ["sales", "marketing", "legal"]):
            continue
        url = item.get("url") or ""
        jobs.append(Job(
            platform="Remote OK", title=title, company=clean_text(item.get("company")),
            location="Remote", url=url, apply_url=url, description=desc,
            published_at=item.get("date", ""), job_type=clean_text(item.get("type")),
            tags=item.get("tags") or [], source_id=stable_id("Remote OK", url, title, item.get("company",""))
        ))
    return jobs
