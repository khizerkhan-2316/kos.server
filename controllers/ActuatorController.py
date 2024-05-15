from flask import jsonify
from flask_cors import cross_origin
from services.ActuatorService import ActuatorService
from flask import request


class ActuatorController:
    def __init__(self, app, actuator_service: ActuatorService):
        self.app = app
        self.actuator_service = actuator_service
        self.register_routes()

    def register_routes(self):
        @cross_origin()
        @self.app.route('/api/v1/actuators', methods=['PUT'])
        async def update_actuator():
            data = request.get_json()

            await self.actuator_service.update_actuator(data.get('id'), data)

            return jsonify("Actuator updated")

        @cross_origin()
        @self.app.route('/api/v1/actuators', methods=['GET'])
        async def get_actuators():
            actuators = await self.actuator_service.get_actuators()
            return jsonify(actuators)
