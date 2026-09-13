"""
Internshala discovery adapter.

The old third-party PyPI package should not be treated as an official API.
This adapter is deliberately disabled by default. Add a verified/allowed
endpoint or connector before enabling it.
"""
def fetch(*args, **kwargs):
    print("Internshala: disabled until a supported current API/feed/connector is configured.")
    return []
