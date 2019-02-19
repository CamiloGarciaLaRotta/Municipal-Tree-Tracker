from flask_restplus import Resource

from server.instance import server
from models.city import city

api = server.api

city_ns = api.namespace('cities', description='city related endpoints')

@city_ns.route('')
class CityList(Resource):
    @api.marshal_list_with(city)
    def get(self):
        """
        Retrieve all cities
        """
        # TODO
        pass

    @api.expect(city, validate=True)
    @api.marshal_with(city)
    def post(self):
        """
        Create a new city
        """
        # TODO
        pass

@city_ns.route('/<string:c_name>')
class Tree(Resource):
    @api.marshal_with(city)
    def get(self, c_name):
        """
        Retrieve a specific city
        """
        # TODO
        pass

    @api.marshal_with(city)
    def delete(self, c_name):
        """
        Delete a specific city
        """
        # TODO
        pass

    @api.expect(city, validate=True)
    @api.marshal_with(city)
    def put(self, c_name):
        """
        Update a specific city
        """
        # TODO
        pass
