from flask_restplus import fields
from server.instance import server

user_types = ['URBAN_PLANNER', 'ENV_SCIENTIST', 'RESIDENT']

user = server.api.model('User', {
    'uid': fields.String(
        example='123',
        description='User ID'),
    'u_type': fields.String(
        required=True,
        example='RESIDENT',
        description='User type'),
    'u_name': fields.String(
        required=True,
        example='Johanne Doe',
        description='Name of the user'),
    'u_email': fields.String(
        required=True,
        example='jdoe@foobar.com',
        description='Email of the user'),
    'u_phone': fields.String(
        required=True,
        example='5146664141',
        description='Phone number of the user'),
    'civid': fields.String(
        required=True,
        example='123',
        description='Civic address ID of the user'),
})
