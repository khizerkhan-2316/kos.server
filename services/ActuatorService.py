from data_access.repositories.ActuatorRepository import ActuatorRepository
from dataclasses import asdict


class ActuatorService:
    def __init__(self):
        self.actuator_repo = ActuatorRepository()

    async def get_actuators(self):
        actuators = await self.actuator_repo.get_actuators()

        return actuators
