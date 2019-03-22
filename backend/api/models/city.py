from flask_restplus import fields
from server.instance import server

city = server.api.model('City', {
    'cid': fields.String(
        example='123',
        description='City ID'),
    'c_name': fields.String(
        required=True,
        example='Montreal',
        min_length=1,
        max_length=50,
        description='City name'),
    'c_polygon': fields.String(
        required=True,
        example='((1.0,0.0),(0.0,0.0),(2.0,3.0))',
        description='City\'s polygon in Postgres Polygon format'),
})

works_for = server.api.model('Works_for', {
    'start_date': fields.Date(
        required=True,
        example='2016-01-01',
        description='Date of start of employment'),
    'cid': fields.String(
        required=True,
        example='123',
        description='ID of the city'),
    'uid': fields.String(
        required=True,
        example='456',
        description='ID of the employee'),
})
