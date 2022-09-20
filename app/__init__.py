from flask import Flask
from flask_restful import Api
from app.resources.session import Session
from app.resources.helloworld import HelloWorld


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource
    api.add_resource(HelloWorld,'/hello')
    api.add_resource(Session, '/session', '/Session/<string:id>')

    return app