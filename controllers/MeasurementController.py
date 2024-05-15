from flask import jsonify, request
from flask_cors import cross_origin
from services.MeasurementService import MeasurementService


class MeasurementController:
    def __init__(self, app, measurement_service: MeasurementService):
        self.app = app
        self.measurement_service = measurement_service
        self.register_routes()

    def register_routes(self):
        @cross_origin()
        @self.app.route('/api/v1/measurements', methods=['GET'])
        async def get_measurements():
            try:
                measurements = await self.measurement_service.get_measurements()
                return jsonify(measurements), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
