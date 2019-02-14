from flask_restplus import fields
from server.instance import server

tree = server.api.model('Tree', {
    'id': fields.Integer(description='Id'),
    'species': fields.String(required=True, example='Acer caesium', min_length=1, max_length=100, description='Scientific name'),
    'planted_on': fields.Date(required=True, example='2015-02-26', description='Date when tree was planted at its current location')
})
