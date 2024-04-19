from flask import jsonify
from flask_cors import cross_origin
from services.ActuatorService import ActuatorService


class ActuatorController:
    def __init__(self, app):
        self.app = app
        self.actuator_service = ActuatorService()
        self.register_routes()

    def register_routes(self):
        @cross_origin()
        @self.app.route('/api/v1/actuators', methods=['GET'])
        async def get_actuators():
            actuators = await self.actuator_service.get_actuators()
            return jsonify(actuators)
