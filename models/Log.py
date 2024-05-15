from dataclasses import dataclass, field
from datetime import datetime
from common.LogLevel import LogLevel
from typing import Dict
import pytz


@dataclass
class Log:
    id: str
    message: str
    level: LogLevel
    created_at: datetime

    def to_dict(self) -> Dict[str, str]:
        self.created_at = pytz.timezone('Europe/Copenhagen').localize(self.created_at)

        return {
            "message": self.message,
            "level": self.level,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, any]) -> 'Log':
        return cls(
            id=data['id'],
            message=data['message'],
            level=data['level'],
            created_at=data['created_at']
        )
