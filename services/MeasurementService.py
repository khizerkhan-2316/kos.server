from datetime import datetime
from services.SerialService import SerialService
from models.Measurement import Measurement
from common.MeasurementType import MeasurementType
from data_access.repositories.MeasurementRepository import MeasurementRepository


class MeasurementService:
    def __init__(self, serial_service: SerialService):
        self.serial_service = serial_service
        self.measurement_repository = MeasurementRepository()

    async def create_measurement(self, measurement_data: str):
        measurements = measurement_data.split(',')

        try:
            # Parse the measurement values
            indoor_temp = float(measurements[0].strip())
            outdoor_temp = float(measurements[1].strip())
            co2_level = float(measurements[2].strip())
        except ValueError as e:
            raise ValueError(f"Invalid measurement data format: {e}")

            # Create a Measurement object using the parsed values
        indoor_measurement = Measurement(id=None,
                                         measurement_type=MeasurementType.INDOOR_TEMPERATURE,
                                         measurement_data=indoor_temp,
                                         created_at=datetime.now())

        outdoor_measurement = Measurement(id=None,
                                          measurement_type=MeasurementType.OUTDOOR_TEMPERATURE,
                                          measurement_data=outdoor_temp,
                                          created_at=datetime.now())

        co2_measurement = Measurement(id=None,
                                      measurement_type=MeasurementType.CO2,
                                      measurement_data=co2_level,
                                      created_at=datetime.now())

        await self.measurement_repository.save_measurement(indoor_measurement)
        await self.measurement_repository.save_measurement(outdoor_measurement)
        await self.measurement_repository.save_measurement(co2_measurement)

    def get_measurement_from_arduino(self, dataset):

        return self.serial_service.send_and_read_command(dataset)

    async def get_measurements(self):
        try:
            measurements = await self.measurement_repository.get_measurements()

            return measurements
        except Exception as e:
            print(f"Error retrieving Measurements: {e}")
            return []
