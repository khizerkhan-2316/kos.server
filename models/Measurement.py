from dataclasses import dataclass
from datetime import datetime
from common.MeasurementType import MeasurementType
from typing import Dict, Any, Optional
import pytz


@dataclass
class Measurement:
    id: Optional[str]  # Making id attribute optional
    measurement_type: MeasurementType
    measurement_data: float
    created_at: datetime

    def to_dict(self) -> Dict[str, Any]:
        if isinstance(self.created_at, str):
            # Parse the string representation of the datetime into a datetime object

            print(self.created_at)

        return {
            "id": self.id,
            "measurement_type": self.measurement_type.value,  # Assuming MeasurementType has a value attribute
            "measurement_data": self.measurement_data,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Measurement':
        """
        Create a Measurement object from a dictionary.

        Args:
            data (dict): Dictionary containing Measurement data.

        Returns:
            Measurement: The created Measurement object.
        """
        return cls(
            id=data['id'],
            measurement_type=data['measurement_type'],  # Convert value string to MeasurementType enum
            measurement_data=data['measurement_data'],
            created_at=data['created_at'])
