from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS
from services.SerialService import SerialService

from controllers.ActuatorController import ActuatorController

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello World"})


cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

actuator_controller = ActuatorController(app)

serial_service = SerialService()

serial_service.open_serial_connection()

serial_service.send_command("T\n")

print("reading")
serial_service.read_status()
print("done reading")

serial_service.close_serial_connection()

if __name__ == '__main__':
    app.run()