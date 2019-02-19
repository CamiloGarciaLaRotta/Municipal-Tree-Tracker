from flask_restplus import fields
from server.instance import server

city = server.api.model('City', {
    'c_name': fields.String(required=True, example='Montreal', min_length=1, max_length=50, description='City name'),
    'c_population': fields.Integer(required=True, example='22348', min=0, description='City\'s population')
})
