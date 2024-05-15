from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Actuator:
    id: str
    name: str
    status: bool
    level: Optional[int]
    type: str
    updated_at: datetime = None

