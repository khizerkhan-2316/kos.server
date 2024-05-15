from data_access.repositories.ActuatorRepository import ActuatorRepository
from dataclasses import asdict
from services.SerialService import SerialService
from services.LoggingService import LoggingService


class ActuatorService:
    def __init__(self, serial_service: SerialService, logging_service: LoggingService):
        self.actuator_repo = ActuatorRepository()
        self.serial_service = serial_service
        self.logging_service = logging_service

    async def update_actuator(self, actuator_id: str, actuator_data):
        if actuator_data.get('status'):
            status = self.serial_service.send_and_read_command(f"Tænd {actuator_data.get('type')}")
        else:
            status = self.serial_service.send_and_read_command(f"Sluk {actuator_data.get('type')}")

    # radiator niveau 1-5 sidst i strengen.

    async def get_actuators_status_from_arduino(self):
        actuators = await self.actuator_repo.get_actuators()

        window_status_command = self.serial_service.send_and_read_command("Hent vindue status")

        window_status = bool(int(window_status_command))  # Assuming the command returns '0' or '1'

        radiator_status_command = self.serial_service.send_and_read_command("Hent radiator status")

        radiator_status = int(radiator_status_command)  # Convert the string to an integer

        for actuator in actuators:
            if actuator.get("type") == 'vindue':
                await self.actuator_repo.update_actuator_status(actuator.get("id"),
                                                                True if window_status else False, window_status)

            else:
                await self.actuator_repo.update_actuator_status(actuator.get("id"),
                                                                True if (1 <= radiator_status <= 5) else False, radiator_status)

    async def get_actuators(self):
        actuators = await self.actuator_repo.get_actuators()
        return actuators
