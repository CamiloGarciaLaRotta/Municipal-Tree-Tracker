from flask_restplus import Resource

from server.instance import server
from models.civic_location import civic_loc

api = server.api

civic_ns = api.namespace('civic_loc', description='civic location related endpoints')

@civic_ns.route('')
class CivicList(Resource):
    @api.marshal_list_with(civic_loc)
    def get(self):
        """
        Retrieve all civic locations
        """
        # TODO
        pass

    @api.expect(civic_loc, validate=True)
    @api.marshal_with(civic_loc)
    def post(self):
        """
        Create a new civic location
        """
        # TODO
        pass

@civic_ns.route('/<int:id>')
class CivicLoc(Resource):
    @api.marshal_with(civic_loc)
    def get(self, id):
        """
        Retrieve a specific civic location
        """
        # TODO
        pass

    @api.marshal_with(civic_loc)
    def delete(self, id):
        """
        Delete a specific civic location
        """
        # TODO
        pass

    @api.expect(civic_loc, validate=True)
    @api.marshal_with(civic_loc)
    def put(self, id):
        """
        Update a specific civic location
        """
        # TODO
        pass
