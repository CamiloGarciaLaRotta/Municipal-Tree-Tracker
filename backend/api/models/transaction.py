from flask_restplus import fields
from server.instance import server
from .tree import tree_species

trans_status = ['PENDING', 'APPROVED', 'REFUSED']

transaction = server.api.model('Transaction', {
    'transid': fields.Integer(
        description='Transaction ID'),
    'trans_status': fields.String(
        required=True,
        example='PENDING',
        description='Transaction status',
        enum=trans_status),
    'tree_species': fields.String(
        required=True,
        example='FIR',
        description='Tree species',
        enum=tree_species),
    'civid': fields.String(
        required=True,
        example='12',
        description='ID of the civic addr. where the tree will be located'),
})
