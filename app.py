from flask import Flask, jsonify
from flask_restx import Api

from controllers.ActuatorController import ActuatorController

app = Flask(__name__)


actuator_controller = ActuatorController(app)

if __name__ == '__main__':
    app.run()
