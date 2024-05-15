from data_access.repositories.LoggingRepository import LoggingRepository
from models.Log import Log
from typing import List


class LoggingService:
    def __init__(self):
        self.repository = LoggingRepository()

    async def create_log(self, log: Log) -> str | None:

        try:
            # Call the save_log method of the repository to save the log
            log_id = await self.repository.save_log(log)
            return log_id  # Return the ID of the created log entry
        except Exception as e:
            # Log the error or handle it as needed
            print(f"Error creating log: {e}")
            return None  # Return None if an error occurs during log creation

    async def get_logs(self) -> List[Log]:
        """
        Retrieve all log entries.

        Returns:
            List[Log]: A list of all log entries.
        """
        try:
            logs = await self.repository.get_logs()
            return logs
        except Exception as e:
            print(f"Error retrieving logs: {e}")
            return []
