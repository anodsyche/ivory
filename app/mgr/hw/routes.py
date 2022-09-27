from flask import Blueprint
from mgr import redis


helloworld = Blueprint('hw',__name__)

@helloworld.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')