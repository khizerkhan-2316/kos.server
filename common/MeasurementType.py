from enum import Enum


class MeasurementType(Enum):
    INDOOR_TEMPERATURE = "INDOOR_TEMPERATURE"
    OUTDOOR_TEMPERATURE = "OUTDOOR_TEMPERATURE"
    CO2 = "CO2"

    @staticmethod
    def from_value(value):
        for member in MeasurementType:
            if member.value == value:
                return member
        raise ValueError(f"{value} is not a valid MeasurementType")
