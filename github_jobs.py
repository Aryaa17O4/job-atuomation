"""
GitHub Jobs legacy adapter.

The historical jobs.github.com service was shut down. Do not call the old
positions.json endpoint. This stub keeps the source visible in the registry.
"""
def fetch(*args, **kwargs):
    print("GitHub Jobs: disabled (legacy service discontinued).")
    return []
