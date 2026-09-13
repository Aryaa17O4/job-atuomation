import requests
from ..models import Job
from ..utils import clean_text, keyword_match, stable_id

URL = "https://remotive.com/api/remote-jobs"

def fetch(keywords, categories=("software-dev","data","devops-sysadmin"), limit=50, timeout=20):
    jobs = []
    for category in categories:
        r = requests.get(URL, params={"category": category, "limit": limit}, timeout=timeout)
        r.raise_for_status()
        for item in r.json().get("jobs", []):
            title = clean_text(item.get("title"))
            desc = clean_text(item.get("description"))
            if not keyword_match(title, desc, keywords, ["sales", "marketing", "legal"]):
                continue
            url = item.get("url", "")
            jobs.append(Job(
                platform="Remotive", title=title, company=clean_text(item.get("company_name")),
                location=clean_text(item.get("candidate_required_location")),
                url=url, apply_url=url, description=desc,
                published_at=item.get("publication_date",""),
                job_type=clean_text(item.get("job_type")),
                tags=item.get("tags") or [],
                source_id=stable_id("Remotive", url, title, item.get("company_name",""))
            ))
    return jobs
