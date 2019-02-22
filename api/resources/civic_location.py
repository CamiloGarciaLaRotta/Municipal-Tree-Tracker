from flask_restplus import Resource

from server.instance import server, db
from models.civic_location import civic_loc
from .dao import get_all, get_by_id, create_single, update_single, delete_by_id

api = server.api

civic_ns = api.namespace(
    'civic_loc', description='civic location related endpoints')


@civic_ns.route('')
class CivicList(Resource):
    @api.marshal_list_with(civic_loc)
    def get(self):
        """Retrieve all civic locations."""
        return get_all('civic_location', db)

    @api.expect(civic_loc, validate=True)
    @api.marshal_with(civic_loc)
    @api.response(409, 'Conflict')
    def post(self):
        """Create a new civic location."""
        attrs = ['civic_addr', 'civic_type']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        record = create_single(vals, attrs, 'civid', 'civic_location', db)
        return record if record else ('Failed to insert', 409)


@civic_ns.route('/<int:civid>')
class CivicLoc(Resource):
    @api.marshal_with(civic_loc)
    @api.response(404, 'Not Found')
    def get(self, civid):
        """Retrieve a specific civic location."""
        record = get_by_id(civid, 'civid', 'civic_location', db)
        return record if record else ('Not Found', 404)

    def delete(self, civid):
        """Delete a specific civic location."""
        delete_by_id(civid, 'civid', 'civic_location', db)

    @api.expect(civic_loc, validate=True)
    @api.marshal_with(civic_loc)
    @api.response(409, 'Conflict')
    def put(self, civid):
        """Update a specific civic location."""
        attrs = ['civic_addr', 'civic_type']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        record = update_single(
            vals, attrs, civid, 'civid', 'civic_location', db)
        return record if record else ('Failed to update', 409)
