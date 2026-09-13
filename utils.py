import hashlib
import re
from datetime import datetime, timezone
from typing import Iterable, List

def clean_text(value) -> str:
    if value is None:
        return ""
    text = re.sub(r"<[^>]+>", " ", str(value))
    return re.sub(r"\s+", " ", text).strip()

def stable_id(platform: str, url: str, title: str, company: str) -> str:
    raw = f"{platform}|{url}|{title}|{company}".lower().strip()
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def dedupe_jobs(jobs: Iterable):
    seen = set()
    out = []
    for job in jobs:
        key = job.url or f"{job.platform}|{job.title}|{job.company}"
        if key in seen:
            continue
        seen.add(key)
        out.append(job)
    return out

def keyword_match(title: str, description: str, keywords: List[str], exclude: List[str]) -> bool:
    haystack = f"{title} {description}".lower()
    if any(word.lower() in haystack for word in exclude):
        return False
    return any(word.lower() in haystack for word in keywords)
