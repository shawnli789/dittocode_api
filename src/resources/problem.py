from flask_jwt_extended import jwt_required
from flask_restful import Resource, request
from flask_sqlalchemy import model
from marshmallow import ValidationError
from models.problem import Problem as ProblemModel
from schemas.problems_schema import ProblemSchema


class Problem(Resource):
    @jwt_required()
    def delete(self, problem_id):
        problem = ProblemModel.find_by_id(problem_id)
        if not problem:
            return {"message": "Problem does not exist"}, 404
        problem.delete()
        return problem.json(), 200

    @jwt_required()
    def put(self, problem_id):
        problem = ProblemModel.find_by_id(problem_id)
        if not problem:
            return {"message": "Problem does not exist"}, 404
        try:
            req = ProblemSchema().load(request.json)
            problem.update(req)
            return problem.json(), 200
        except ValidationError as err:
            return err.messages, 400
            