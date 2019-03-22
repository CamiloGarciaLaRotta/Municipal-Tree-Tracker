from flask import abort
from flask_restplus import Resource

from server.instance import server, db
from models.municipality import municipality
from .dao import (get_all, get_by_id, create_single_by_id,
                  update_by_id, delete_by_attr)

api = server.api

municipality_ns = api.namespace(
    'municipalities', description='municipality related endpoints')


@municipality_ns.route('')
class MunicipalityList(Resource):
    @api.marshal_list_with(municipality)
    def get(self):
        """Retrieve all municipalities."""
        return get_all('municipality', db)

    @api.expect(municipality, validate=True)
    @api.marshal_with(municipality)
    def post(self):
        """Create a new municipality."""
        attrs = ['m_name', 'm_population', 'm_polygon', 'cid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return create_single_by_id(vals, attrs, 'mid', 'municipality', db)
        except Exception as e:
            abort(400, str(e))


@municipality_ns.route('/<int:mid>')
class Municipality(Resource):
    @api.marshal_with(municipality)
    @api.response(404, 'Not Found')
    def get(self, mid):
        """Retrieve a specific municipality."""
        record = get_by_id(mid, 'mid', 'municipality', db)
        return record if record else ('Not Found', 404)

    def delete(self, mid):
        """Delete a specific municipality."""
        delete_by_attr([mid], ['mid'], 'municipality', db)

    @api.expect(municipality, validate=True)
    @api.marshal_with(municipality)
    def put(self, mid):
        """Update a specific municipality."""
        attrs = ['m_name', 'm_population', 'm_polygon', 'cid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return update_by_id(vals, attrs, mid, 'mid', 'municipality', db)
        except Exception as e:
            abort(400, str(e))
