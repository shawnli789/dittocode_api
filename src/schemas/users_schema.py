from marshmallow import fields, Schema, validate


class UserSignUpSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=5, max=30))
    email = fields.Email(required=True, validate=validate.Length(min=3, max=254))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=128))

class UserLoginSchema(Schema):
    user_identifier = fields.Str(required=True, validate=validate.Length(max=254))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=128))