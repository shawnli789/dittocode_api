from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request
from marshmallow import ValidationError
from models.problem import Problem
from schemas.problems_schema import ProblemValidatorSchema


class ProblemValidator(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        try:
            req = ProblemValidatorSchema().load(request.json)
            print("req", req)
            req["user_id"] = user_id
            print("user_id", user_id)
            return req, 200
        except ValidationError as err:
            return err.messages, 400