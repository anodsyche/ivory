# compose_flask/app.py
from flask import Flask
from redis import Redis
from flask_redisboard import RedisBoardExtension


board = RedisBoardExtension()
redis = Redis(host='redis', port=6379)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456'
    board.init_app(app)
    from mgr.hw.routes import helloworld
    app.register_blueprint(helloworld)

    return app

#eof