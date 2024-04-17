from flask import jsonify


class ActuatorController:
    def __init__(self, app):
        self.app = app

        self.register_routes()

    def register_routes(self):
        @self.app.route('/api/v1/actuators', methods=['GET'])
        def get_actuators():
            return jsonify({"message": "GET Request"})
