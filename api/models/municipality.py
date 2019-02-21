from flask_restplus import fields
from server.instance import server

municipality = server.api.model('Municipality', {
    'mid': fields.String(
        example='123',
        description='Municipality ID'),
    'm_name': fields.String(
        required=True,
        example='St-Henri',
        min_length=1,
        max_length=50,
        description='Municipality name'),
    'm_population': fields.Integer(
        required=True,
        example='22348',
        min=0,
        description='Municipality\'s population'),
    'm_polygon': fields.String(
        required=True,
        example='((1.0,0.0),(0.0,0.0),(2.0,3.0))',
        description='Municipality\'s polygon in Postgres Polygon format'),
    'c_name': fields.String(
        example='Montreal',
        min_length=1, max_length=50,
        description='City name to which the municipality belongs'),
})
