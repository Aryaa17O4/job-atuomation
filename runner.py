import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from .registry import SOURCES
from .utils import dedupe_jobs

DEFAULT_KEYWORDS = [
    "software engineer intern", "software engineer", "SDE intern",
    "backend intern", "backend developer", "python developer",
    "full stack intern", "full stack developer", "frontend intern",
    "machine learning intern", "AI engineer", "data engineer",
    "FastAPI", "React", "PyTorch"
]

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

def _fetch(source, keywords):
    try:
        return source["module"].fetch(keywords)
    except Exception as exc:
        logging.exception("%s failed: %s", source["name"], exc)
        return []

def collect(keywords=None, workers=6):
    keywords = keywords or DEFAULT_KEYWORDS
    results = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(_fetch, source, keywords): source
            for source in SOURCES if source["enabled"]
        }
        for future in as_completed(futures):
            source = futures[future]
            jobs = future.result()
            logging.info("%s: %d jobs", source["name"], len(jobs))
            results.extend(jobs)
    return dedupe_jobs(results)

def save_json(jobs, path="jobs.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([j.to_dict() for j in jobs], f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    jobs = collect()
    save_json(jobs)
    print(f"Total unique jobs: {len(jobs)}")
