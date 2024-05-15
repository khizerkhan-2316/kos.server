import asyncio
import threading

from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS
from services.SerialService import SerialService
from services.ActuatorService import ActuatorService
from services.LoggingService import LoggingService
from services.MeasurementService import MeasurementService
from controllers.ActuatorController import ActuatorController
from controllers.LoggingController import LoggingController
from controllers.MeasurementController import MeasurementController
import time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Create services
serial_service = SerialService()
logging_service = LoggingService()
actuator_service = ActuatorService(serial_service, logging_service)
measurement_service = MeasurementService(serial_service)

# Create controllers
actuator_controller = ActuatorController(app, actuator_service)
measurement_controller = MeasurementController(app, measurement_service)
logging_controller = LoggingController(app, logging_service)

serial_service.open_serial_connection()

time.sleep(5)

dataset_number = 1


async def test():
    while True:
        try:
            await actuator_service.get_actuators_status_from_arduino()
            print("ACTUACTORS UPDATED FROM THREAD!!")
        except Exception as e:
            print("An error occurred:", e)

        # Wait for 10 seconds before the next iteration
        await asyncio.sleep(60)


# Define function to get measurements
async def get_measurements():
    global dataset_number  # Access the global variable
    while True:
        try:
            # Formulate dataset name (e.g., D1, D2, D3, ...)
            dataset = f"D{dataset_number}"

            # Get measurement data
            data = measurement_service.get_measurement_from_arduino(dataset=dataset)

            # Create measurement
            await measurement_service.create_measurement(data)
            print("Measurement retrieved successfully:", data)

            # Increment dataset number for the next iteration
            dataset_number += 1
        except Exception as e:
            print("An error occurred:", e)

        # Wait for 10 seconds before the next iteration
        await asyncio.sleep(10)


actuator_status_thread = threading.Thread(target=asyncio.run, args=(test(),))
actuator_status_thread.start()

measurement_thread = threading.Thread(target=asyncio.run, args=(get_measurements(),))
measurement_thread.start()

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
