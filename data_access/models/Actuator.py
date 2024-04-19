from dataclasses import dataclass


@dataclass
class Actuator:
    id: str
    name: str
    status: bool
    type: str
