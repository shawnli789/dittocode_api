from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.healthCheck import HealthCheck
from resources.problem import Problem
from resources.problems import Problems
from resources.problemValidator import ProblemValidator
from resources.sessions import Sessions
from resources.user import User
from resources.users import Users


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# set the configuration
if app.config["ENV"] == "production":
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["PROD_DB"]
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DEV_DB"]

@app.before_first_request
def create_tables():
    db.create_all()

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

api.add_resource(User, '/user/')
api.add_resource(Users, '/users/')
api.add_resource(Problem, '/problems/<int:problem_id>')
api.add_resource(Problems, '/problems/')
api.add_resource(Sessions, '/sessions/')
api.add_resource(ProblemValidator, '/problem-validator/')
api.add_resource(HealthCheck, '/health-check/')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run()


