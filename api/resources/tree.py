from flask_restplus import Resource

from server.instance import server, db
from models.tree import tree, tree_species
from .dao import get_all, get_by_id, create_single, update_single, delete_by_id

api = server.api

tree_ns = api.namespace('trees', description='tree related endpoints')


@tree_ns.route('/species')
class TreeSpecies(Resource):
    def get(self):
        """Retrieve all tree species."""
        return {'species': tree_species}


@tree_ns.route('')
class TreeList(Resource):
    @api.marshal_list_with(tree)
    def get(self):
        """Retrieve all trees."""
        return get_all('tree', db)

    @api.expect(tree, validate=True)
    @api.marshal_with(tree)
    @api.response(409, 'Conflict')
    def post(self):
        """Create a new tree."""
        # TODO how to handle optional values
        attrs = ['species', 'planted_date', 'geog_loc']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        record = create_single(vals, attrs, 'tid', 'tree', db)
        return record if record else ('Failed to insert', 409)


@tree_ns.route('/<int:tid>')
class Tree(Resource):
    @api.marshal_with(tree)
    @api.response(404, 'Not Found')
    def get(self, tid):
        """Retrieve a specific tree."""
        record = get_by_id(tid, 'tid', 'tree', db)
        return record if record else ('Not Found', 404)

    def delete(self, tid):
        """Delete a specific tree."""
        delete_by_id(tid, 'tid', 'tree', db)

    @api.expect(tree, validate=True)
    @api.marshal_with(tree)
    @api.response(409, 'Conflict')
    def put(self, tid):
        """Update a specific tree."""
        attrs = ['species', 'planted_date', 'geog_loc']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        record = update_single(vals, attrs, tid, 'tid', 'tree', db)
        return record if record else ('Failed to update', 409)
