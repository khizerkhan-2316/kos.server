from flask import jsonify, request
from flask_cors import cross_origin
from services.LoggingService import LoggingService


class LoggingController:
    def __init__(self, app, logging_service: LoggingService):
        self.app = app
        self.logging_service = logging_service
        self.register_routes()

    def register_routes(self):
        @cross_origin()
        @self.app.route('/api/v1/logs', methods=['POST'])
        async def create_log():
            try:
                data = request.get_json()
                log_id = await self.logging_service.create_log(data)
                return jsonify({"message": "Log created", "log_id": log_id}), 201
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @cross_origin()
        @self.app.route('/api/v1/logs', methods=['GET'])
        async def get_logs():
            try:
                logs = await self.logging_service.get_logs()
                return jsonify(logs), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
