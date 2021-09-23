from db import db
from flask_restful import Resource, request
from marshmallow import ValidationError
from models.user import User
from schemas.users_schema import UserSignUpSchema


class Users(Resource):        
    def post(self):
        try:
            req = UserSignUpSchema().load(request.json)
            message = {}
            if User.find_by_email(req['email']):
                message["email"] = ["Email already exists"]
            if User.find_by_username(username=req['username']):
                message["username"] = ["Username already exists"]
            if message:
                return message, 400
            new_user = User(**req)
            new_user.hash_password()
            new_user.save()
            return new_user.json(), 200
        except ValidationError as err:
            return err.messages, 400



