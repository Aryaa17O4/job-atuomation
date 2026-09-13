import requests
from ..models import Job
from ..utils import clean_text, keyword_match, stable_id

URL = "https://himalayas.app/jobs/api"

def fetch(keywords, max_pages=5, timeout=20):
    jobs, cursor = [], None
    for _ in range(max_pages):
        params = {"limit": 20}
        if cursor:
            params["cursor"] = cursor
        r = requests.get(URL, params=params, timeout=timeout)
        r.raise_for_status()
        data = r.json()
        for item in data.get("jobs", []):
            title = clean_text(item.get("title"))
            desc = clean_text(item.get("description") or item.get("excerpt"))
            if not keyword_match(title, desc, keywords, ["sales", "marketing", "legal"]):
                continue
            url = item.get("applicationLink") or ""
            jobs.append(Job(
                platform="Himalayas", title=title, company=clean_text(item.get("companyName")),
                location=", ".join(item.get("locationRestrictions") or []) or "Remote",
                url=url, apply_url=url, description=desc,
                published_at=item.get("pubDate",""),
                job_type=clean_text(item.get("employmentType")),
                tags=item.get("category") or [],
                source_id=stable_id("Himalayas", url or item.get("guid",""), title, item.get("companyName","")),
                metadata={"salary_min": item.get("minSalary"), "salary_max": item.get("maxSalary"),
                          "currency": item.get("currency"), "guid": item.get("guid")}
            ))
        cursor = data.get("nextCursor")
        if not cursor:
            break
    return jobs
