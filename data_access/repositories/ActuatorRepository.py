from data_access.db_utils import DBUtils


class ActuatorRepository:
    def __init__(self):
        self.dbUtils = DBUtils()
        self.collection_name = "actuators"

    async def update_actuator_status(self, actuator_id, new_status, level):
        update_data = {"status": new_status, "level": level}
        await self.dbUtils.update_document(self.collection_name, actuator_id, update_data)

    async def get_actuators(self):

        return await self.dbUtils.get_all_documents(self.collection_name)


