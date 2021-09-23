from marshmallow import fields, Schema, validate


class ProblemSchema(Schema):
    number = fields.Int(required=True, validate=validate.Range(min=0, max=1000000))
    title = fields.Str(required=True, validate=validate.Length(max=128))
    type = fields.Str(required=True, validate=validate.Length(max=30))
    difficulty = fields.Str(required=True, validate=validate.Length(max=30))
    tags = fields.Str(required=True, validate=validate.Length(max=300))
    completed = fields.Bool(required=True)
    url = fields.Str(validate=validate.Length(max=3000))
    time_spent = fields.Int(required=True, validate=validate.Range(min=0, max=120))

class ProblemValidatorSchema(Schema):
    number = fields.Int(required=True, validate=validate.Range(min=0, max=1000000))
    title = fields.Str(required=True, validate=validate.Length(max=128))
    type = fields.Str(required=True, validate=validate.Length(max=30))
    difficulty = fields.Str(required=True, validate=validate.Length(max=30))
    tags = fields.Str(required=True, validate=validate.Length(max=300))
    url = fields.Str(validate=validate.Length(max=3000))