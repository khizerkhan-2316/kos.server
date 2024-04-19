from ..db_utils import DBUtils


class ActuatorRepository:
    def __init__(self):
        self.dbUtils = DBUtils()

    async def get_actuators(self):
        collection_name = "actuators"
        return await self.dbUtils.get_all_documents(collection_name)
