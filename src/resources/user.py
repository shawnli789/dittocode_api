from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, request
from marshmallow import ValidationError
from models.problem import Problem as ProblemModel
from models.user import User as UserModel
from schemas.users_schema import UserSignUpSchema


class User(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)
        return user.json(), 200

    @jwt_required()
    def put(self):
        user_id = get_jwt_identity()
        user = UserModel.find_by_id(user_id)
        try:
            req = UserSignUpSchema().load(request.json)
            user.update(req)
            return user.json(), 200
        except ValidationError as err:
            return err.messages, 400

    @jwt_required()
    def delete(self):
        user_id = get_jwt_identity()

        # Delete all the problems
        problems = ProblemModel.find_all_by_user_id(user_id)
        for p in problems:
            p.delete()

        # Delete the user
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete()
            return user.json(), 200
        else:
            return {"message": "User does not exist"}, 404
