from flask_restplus import Resource

from server.instance import server
from models.park import park

api = server.api

park_ns = api.namespace('parks', description='park related endpoints')

@park_ns.route('')
class ParkList(Resource):
    @api.marshal_list_with(park)
    def get(self):
        """
        Retrieve all parks
        """
        # TODO
        pass

    @api.expect(park, validate=True)
    @api.marshal_with(park)
    def post(self):
        """
        Create a new park
        """
        # TODO
        pass

@park_ns.route('/<string:p_name>')
class Park(Resource):
    @api.marshal_with(park)
    def get(self, p_name):
        """
        Retrieve a specific park
        """
        # TODO
        pass

    @api.marshal_with(park)
    def delete(self, p_name):
        """
        Delete a specific park
        """
        # TODO
        pass

    @api.expect(park, validate=True)
    @api.marshal_with(park)
    def put(self, p_name):
        """
        Update a specific park
        """
        # TODO
        pass
