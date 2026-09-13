from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List

@dataclass
class Job:
    platform: str
    title: str
    company: str = ""
    location: str = ""
    url: str = ""
    description: str = ""
    published_at: str = ""
    job_type: str = ""
    tags: List[str] = field(default_factory=list)
    source_id: str = ""
    apply_url: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
