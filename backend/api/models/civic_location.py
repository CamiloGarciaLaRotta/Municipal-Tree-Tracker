from flask_restplus import fields
from server.instance import server

civic_loc_type = ['RESIDENTIAL', 'INDUSTRIAL', 'COMERCIAL', 'FARM']

civic_loc = server.api.model('Civic_loc', {
    'civid': fields.String(
        example='123',
        description='Civic location ID'),
    'civic_addr': fields.String(
        required=True,
        example='3700 Ave. Benny',
        min_length=1,
        max_length=50,
        description='Civic address'),
    'civic_type': fields.String(
        required=True,
        example='COMERCIAL',
        description='Land usage type',
        enum=civic_loc_type),
})
