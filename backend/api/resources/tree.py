import sys
from flask import abort
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
    def post(self):
        """Create a new tree."""
        attrs = ['species', 'planted_date', 'geog_loc', 'mid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        if api.payload['pid']:
            attrs.append('pid')
            vals.append(api.payload['pid'])
        if api.payload['civid']:
            attrs.append('civid')
            vals.append(api.payload['civid'])
        try:
            return create_single(vals, attrs, 'tid', 'tree', db)
        except Exception as e:
            abort(400, str(e))


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
    def put(self, tid):
        """Update a specific tree."""
        attrs = ['species', 'planted_date', 'geog_loc', 'mid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        if api.payload['pid']:
            attrs.append('pid')
            vals.append(api.payload['pid'])
        if api.payload['civid']:
            attrs.append('civid')
            vals.append(api.payload['civid'])
        try:
            return update_single(vals, attrs, tid, 'tid', 'tree', db)
        except Exception as e:
            abort(400, str(e))
