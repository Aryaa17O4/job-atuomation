"""
Indeed adapter.

Indeed's historical RSS/search behavior is not a stable public API contract.
Keep this source disabled unless the exact current permitted feed/API is
configured for the deployment.
"""
def fetch(*args, **kwargs):
    print("Indeed: disabled until a supported current feed/API is configured.")
    return []
