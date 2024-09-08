# Foundations of the Flask App

# Web development imports
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

# Environment variables
from config import *

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

# Routes
from routes import *

if __name__ == '__main__':
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )