"""
Stack Overflow Jobs legacy adapter.

The historical Stack Overflow Jobs feed/service is no longer a dependable live
source. This adapter intentionally returns no jobs instead of pretending the
old endpoint works. Keep the platform in the registry so it can be re-enabled
if a supported feed/API becomes available.
"""
def fetch(*args, **kwargs):
    print("Stack Overflow Jobs: disabled (legacy source; no reliable live endpoint configured).")
    return []
