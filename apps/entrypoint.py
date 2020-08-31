import os

from flasgger import Swagger
from flask import Flask
from flask_jwt_extended import JWTManager

from apps import api
from apps.api import context

app = Flask(__name__)
context = context.Context()

app.config["SWAGGER"] = {
    "uiversion": 3,
    "openapi": "3.0.2",
}
swagger = Swagger(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "lDI\x05b\x02w\x92\x1a\x05hmdW\xcb\xcaa\xef\xae\xac"
jwt = JWTManager(app)

app.register_blueprint(api.bp)

if os.getenv("FLASK_ENV") == "development":
    from apps import demo

    app.register_blueprint(demo.bp)
