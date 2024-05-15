from typing import List
from data_access.db_utils import DBUtils
from models.Log import Log


class LoggingRepository:
    def __init__(self):
        self.dbUtils = DBUtils()
        self.collection_name = "logs"

    async def save_log(self, log: Log):
        try:
            log_data = log.to_dict()
            document_id = await self.dbUtils.add_document(self.collection_name, log_data)
            return document_id
        except Exception as e:
            # Log the error or handle it as needed
            print(f"Error saving log: {e}")
            return None

    async def get_logs(self) -> List[Log]:
        documents = await self.dbUtils.get_all_documents(self.collection_name)
        logs = [Log.from_dict(doc) for doc in documents]
        return logs
