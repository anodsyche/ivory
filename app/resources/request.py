from flask_restful import Resource

class GoalRequest(Resource):
    def get(self):
        return {'hello': 'world'}