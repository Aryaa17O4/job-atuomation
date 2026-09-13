from .platforms import remoteok, remotive, himalayas, weworkremotely, jobspresso
from .platforms import workingnomads, devto, stack_overflow, github_jobs, hiring_threads
from .platforms import aicte, internshala, foundit, indeed, simplify

SOURCES = [
    {"name": "Remote OK", "module": remoteok, "mode": "api", "enabled": True},
    {"name": "Remotive", "module": remotive, "mode": "api", "enabled": True},
    {"name": "Himalayas", "module": himalayas, "mode": "api", "enabled": True},
    {"name": "We Work Remotely", "module": weworkremotely, "mode": "rss", "enabled": True},
    {"name": "Jobspresso", "module": jobspresso, "mode": "rss", "enabled": True},
    {"name": "Working Nomads", "module": workingnomads, "mode": "rss", "enabled": True},
    {"name": "GitHub Jobs", "module": github_jobs, "mode": "legacy-disabled", "enabled": True},
    {"name": "Stack Overflow Jobs", "module": stack_overflow, "mode": "legacy-disabled", "enabled": True},
    {"name": "DEV Community Jobs", "module": devto, "mode": "rss", "enabled": True},
    {"name": "HN Who's Hiring", "module": hiring_threads, "mode": "hn-api", "enabled": True},
    {"name": "AICTE", "module": aicte, "mode": "placeholder", "enabled": True},
    {"name": "Internshala", "module": internshala, "mode": "placeholder", "enabled": True},
    {"name": "Foundit", "module": foundit, "mode": "scrape-discovery", "enabled": True},
    {"name": "Indeed", "module": indeed, "mode": "placeholder", "enabled": True},
    {"name": "Simplify Jobs", "module": simplify, "mode": "placeholder", "enabled": True},
]
