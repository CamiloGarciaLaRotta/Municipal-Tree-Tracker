from flask import abort
from flask_restplus import Resource

from server.instance import server, db
from models.transaction import transaction, trans_status
from .dao import (get_all, get_by_id, create_single_by_id,
                  update_by_id, delete_by_attr)

api = server.api

trans_ns = api.namespace(
    'transaction', description='transaction transaction related endpoints')


@trans_ns.route('/status')
class TransStatus(Resource):
    def get(self):
        """Retrieve all transaction status."""
        return {'status': trans_status}


@trans_ns.route('')
class TransList(Resource):
    @api.marshal_list_with(transaction)
    def get(self):
        """Retrieve all transactions for a tree."""
        return get_all('transactions', db)

    @api.expect(transaction, validate=True)
    @api.marshal_with(transaction)
    def post(self):
        """Create a new transaction."""
        ks = ['trans_status', 'tree_species', 'civid']
        vs = list(map(lambda attr: api.payload[attr], ks))
        try:
            return create_single_by_id(vs, ks, 'transid', 'transactions', db)
        except Exception as e:
            abort(400, str(e))


@trans_ns.route('/<int:transid>')
class Trans(Resource):
    @api.marshal_with(transaction)
    @api.response(404, 'Not Found')
    def get(self, transid):
        """Retrieve a specific transaction."""
        record = get_by_id(transid, 'transid', 'transactions', db)
        return record if record else ('Not Found', 404)

    # def delete(self, transid):
    #     """Delete a specific transaction."""
    #     delete_by_attr([transid], ['transid'], 'transactions', db)

    @api.expect(transaction, validate=True)
    @api.marshal_with(transaction)
    def put(self, transid):
        """Update a specific transaction."""
        ks = ['trans_status', 'tree_species', 'civid']
        vs = list(map(lambda attr: api.payload[attr], ks))
        try:
            return update_by_id(vs, ks, transid,
                                'transid', 'transactions', db)
        except Exception as e:
            abort(400, str(e))
