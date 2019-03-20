from flask import abort
from flask_restplus import Resource

from server.instance import server, db
from models.city import city
from .dao import get_all, get_by_id, create_single, update_single, delete_by_id

api = server.api

city_ns = api.namespace('cities', description='city related endpoints')


@city_ns.route('')
class CityList(Resource):
    @api.marshal_list_with(city)
    def get(self):
        """Retrieve all cities."""
        return get_all('city', db)

    @api.expect(city, validate=True)
    @api.marshal_with(city)
    def post(self):
        """Create a new city."""
        attrs = ['c_name', 'c_polygon']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return create_single(vals, attrs, 'cid', 'city', db)
        except Exception as e:
            abort(400, str(e))


@city_ns.route('/<int:cid>')
class City(Resource):
    @api.marshal_with(city)
    @api.response(404, 'Not Found')
    def get(self, cid):
        """Retrieve a specific city."""
        record = get_by_id(cid, 'cid', 'city', db)
        return record if record else ('Not Found', 404)

    def delete(self, cid):
        """Delete a specific city."""
        delete_by_id(cid, 'cid', 'city', db)

    @api.expect(city, validate=True)
    @api.marshal_with(city)
    @api.response(409, 'Conflict')
    def put(self, cid):
        attrs = ['c_name', 'c_polygon']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return update_single(vals, attrs, cid, 'cid', 'city', db)
        except Exception as e:
            abort(400, str(e))
