import platform

from dataclasses import dataclass
from typing import Dict


@dataclass
class Test:
    name: str
    platform: str
    oncall: str

    @classmethod
    def from_bazel_event(cls, event: Dict[str, any], team: str):
        return cls(
            name=event["id"]["testResult"]["label"],
            platform=platform.system(),
            oncall=team,
        )
