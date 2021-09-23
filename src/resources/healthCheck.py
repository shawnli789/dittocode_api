from flask_restful import Resource


class HealthCheck(Resource):
    def get(self):
        return "200 Okay", 200