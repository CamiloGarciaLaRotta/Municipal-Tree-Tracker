from flask_restplus import Resource

from server.instance import server, db
from models.park import park
from .dao import get_all, get_by_id, create_single, update_single, delete_by_id

api = server.api

park_ns = api.namespace('parks', description='park related endpoints')


@park_ns.route('')
class ParkList(Resource):
    @api.marshal_list_with(park)
    def get(self):
        """Retrieve all parks."""
        return get_all('park', db)

    @api.expect(park, validate=True)
    @api.marshal_with(park)
    @api.response(409, 'Conflict')
    def post(self):
        """Create a new park."""
        # TODO how to handle optional values
        attrs = ['p_name', 'p_polygon']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        record = create_single(vals, attrs, 'pid', 'park', db)
        return record if record else ('Failed to insert', 409)


@park_ns.route('/<int:pid>')
class Park(Resource):
    @api.marshal_with(park)
    @api.response(404, 'Not Found')
    def get(self, pid):
        """Retrieve a specific park."""
        record = get_by_id(pid, 'pid', 'park', db)
        return record if record else ('Not Found', 404)

    def delete(self, pid):
        """Delete a specific park."""
        delete_by_id(pid, 'pid', 'park', db)

    @api.expect(park, validate=True)
    @api.marshal_with(park)
    @api.response(409, 'Conflict')
    def put(self, pid):
        """Update a specific park."""
        attrs = ['p_name', 'p_polygon']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        record = update_single(vals, attrs, pid, 'pid', 'park', db)
        return record if record else ('Failed to update', 409)
