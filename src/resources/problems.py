from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request
from marshmallow import ValidationError
from models.problem import Problem
from schemas.problems_schema import ProblemSchema
import time


class Problems(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        return {'problems': [x.json() for x in Problem.find_all_by_user_id(user_id)]}, 200

    @jwt_required()
    
    def post(self):
        time.sleep(0.8)
        user_id = get_jwt_identity()
        try:
            req = ProblemSchema().load(request.json)
            req["user_id"] = user_id
            new_problem = Problem(**req)
            new_problem.save()
            return new_problem.json(), 200
        except ValidationError as err:
            return err.messages, 400


        
        
