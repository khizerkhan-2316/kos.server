from data_access.db_utils import DBUtils
from models.Measurement import Measurement
from typing import List


class MeasurementRepository:
    def __init__(self):
        self.dbUtils = DBUtils()
        self.collection_name = "measurements"  # Assuming "measurements" is the correct collection name

    async def save_measurement(self, measurement: Measurement):
        try:
            measurement_data = measurement.to_dict()  # Assuming Measurement has a to_dict() method
            document_id = await self.dbUtils.add_document(self.collection_name, measurement_data)
            return document_id
        except Exception as e:
            # Log the error or handle it as needed
            print(f"Error saving measurement: {e}")
            return None

    async def get_measurements(self) -> List[Measurement]:
        documents = await self.dbUtils.get_all_documents(self.collection_name)
        measurements = [Measurement.from_dict(doc) for doc in documents]  # Assuming Measurement has a from_dict() method
        return measurements
