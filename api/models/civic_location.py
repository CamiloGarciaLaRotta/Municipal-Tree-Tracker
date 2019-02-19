from flask_restplus import fields
from server.instance import server

civic_loc = server.api.model('Civic Location', {
    # TODO maybe add an ID field
    'civic_addr': fields.String(required=True, example='3700 Ave. Benny', min_length=1, max_length=50, description='Civic address'),
    'civic_type': fields.String(required=True, example='COMERCIAL', description='Land usage type', enum=['RESIDENTIAL', 'INDUSTRIAL', 'COMERCIAL', 'FARM'])
})
