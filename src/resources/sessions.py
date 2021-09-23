import datetime
from db import db
from flask_jwt_extended import create_access_token
from flask_restful import Resource, request
from marshmallow import ValidationError
from models.user import User
from schemas.users_schema import UserLoginSchema
			

class Sessions(Resource):
	def post(self):
		try:
			req = UserLoginSchema().load(request.json)
			user_identifier = req["user_identifier"]
			message = {}
			#Check user exists
			if "@" in user_identifier:
				user = User.query.filter_by(email=user_identifier).first()
				if not user:
					message["user_identifier"] = ["Email does not exist"]
			else:
				user = User.query.filter_by(username=user_identifier).first()
				if not user:
					message["user_identifier"] = ["Username does not exist"]
			if message:
				return message, 404

			#Check credentials
			authorized = user.check_password(req['password'])
			if not authorized:
				message["password"] = ["Credentials you specified are not correct"]
				return message, 401

			expires = datetime.timedelta(days=7)
			access_token = create_access_token(identity=user.id, expires_delta=expires)
			return {'token': access_token}, 200
		except ValidationError as err:
			print(err.message)
			return err.messages, 400

