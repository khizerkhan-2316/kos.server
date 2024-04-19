from flask import Flask, jsonify
from flask_restx import Api
from flask_cors import CORS


from controllers.ActuatorController import ActuatorController

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

actuator_controller = ActuatorController(app)



if __name__ == '__main__':
    app.run()
