from flask_restplus import fields
from server.instance import server

park = server.api.model('Park', {
    'pid': fields.String(
        example='123',
        description='Park ID'),
    'p_name': fields.String(
        required=True,
        example='St-Henri',
        min_length=1,
        max_length=50,
        description='Park name'),
    'p_polygon': fields.String(
        required=True,
        example='((1.0,0.0),(0.0,0.0),(2.0,3.0))',
        description='Park\'s polygon in Postgres Polygon format'),
    'mid': fields.String(
        required=True,
        example='169',
        description='ID of the municipality to which the park belongs')
})
