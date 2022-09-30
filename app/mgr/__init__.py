# compose_flask/app.py
from readline import redisplay
from flask import Flask
from flask_redis import FlaskRedis
from redis_om import Migrator
from redis_om import MigrationError


redis = FlaskRedis()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456'
    app.config['REDIS_URL'] = 'redis://redis:6379'
    redis.init_app(app)
    with app.app_context():
        from .hw.routes import helloworld
        app.register_blueprint(helloworld)
        Migrator().run()
        return app
#eof