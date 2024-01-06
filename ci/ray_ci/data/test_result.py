import os
import time
from typing import Dict
from dataclasses import dataclass

from ci.ray_ci.data.test import Test
from ci.ray_ci.utils import logger


@dataclass
class TestResult:
    test: Test
    status: str
    commit: str
    url: str
    timestamp: int

    @classmethod
    def from_bazel_event(cls, event: Dict[str, any]):
        return cls(
            test=Test.from_bazel_event(event),
            status=event["testResult"]["status"],
            commit=os.environ.get("BUILDKITE_COMMIT"),
            url=(
                f"{os.environ.get('BUILDKITE_BUILD_URL')}"
                f"#{os.environ.get('BUILDKITE_JOB_ID')}"
            ),
            timestamp=int(time.time() * 1000),
        )

    def upload(self) -> None:
        # TODO(can): to be implemented
        logger.info(f"Uploading test result: {self}")
        pass
