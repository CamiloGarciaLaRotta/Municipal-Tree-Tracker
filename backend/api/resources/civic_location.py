from flask import abort
from flask_restplus import Resource

from server.instance import server, db
from models.civic_location import civic_loc, civic_loc_type
from .dao import (get_all, get_by_id, create_single_by_id,
                  update_by_id, delete_by_attr)

api = server.api

civic_ns = api.namespace(
    'civic_loc', description='civic location related endpoints')


@civic_ns.route('/types')
class CivicType(Resource):
    def get(self):
        """Retrieve all civic location types."""
        return {"types": civic_loc_type}


@civic_ns.route('')
class CivicList(Resource):
    @api.marshal_list_with(civic_loc)
    def get(self):
        """Retrieve all civic locations."""
        return get_all('civic_location', db)

    @api.expect(civic_loc, validate=True)
    @api.marshal_with(civic_loc)
    def post(self):
        """Create a new civic location."""
        attrs = ['civic_address', 'civic_type']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return create_single_by_id(vals, attrs, 'civid',
                                       'civic_location', db)
        except Exception as e:
            abort(400, str(e))


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
        delete_by_attr([civid], ['civid'], 'civic_location', db)

    @api.expect(civic_loc, validate=True)
    @api.marshal_with(civic_loc)
    def put(self, civid):
        """Update a specific civic location."""
        attrs = ['civic_address', 'civic_type']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return update_by_id(
                vals, attrs, civid, 'civid', 'civic_location', db)
        except Exception as e:
            abort(400, str(e))
