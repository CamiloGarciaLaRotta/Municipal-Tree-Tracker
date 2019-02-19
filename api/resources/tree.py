from flask_restplus import Resource

from server.instance import server
from models.tree import tree

# Dummy example to ensure connectivity
import records
from environment.instance import environment_config
db_user     = environment_config['db_user']
db_pass     = environment_config['db_pass']
db_server   = environment_config['db_server']
db_name     = environment_config['db_name']

db = records.Database(f'postgres://{db_user}:{db_pass}@{db_server}/{db_name}')
rows = db.query('select * from city')
print(rows[0])
##################################

api = server.api

trees_db = [
    {"id": 0, "species": "Acacia penninervis", "planted_on":"2014-02-15"},
    {"id": 1, "species": "Prunus dulcis", "planted_on":"2014-12-01"},
]

tree_ns = api.namespace('trees', description='tree related endpoints')

@tree_ns.route('')
class TreeList(Resource):
    @api.marshal_list_with(tree)
    def get(self):
        """
        Retrieve all trees
        """
        return trees_db

    @api.expect(tree, validate=True)
    @api.marshal_with(tree)
    def post(self):
        """
        Create a new tree
        """
        api.payload["id"] = trees_db[-1]["id"] + 1 if len(trees_db) > 0 else 0
        trees_db.append(api.payload)
        return api.payload

@tree_ns.route('/<int:id>')
class Tree(Resource):
    def find_one(self, id):
        return next((b for b in trees_db if b["id"] == id), None)

    @api.marshal_with(tree)
    def get(self, id):
        """
        Retrieve a specific tree
        """
        match = self.find_one(id)
        return match if match else ("Not found", 404)

    @api.marshal_with(tree)
    def delete(self, id):
        """
        Delete a specific tree
        """
        global trees_db
        match = self.find_one(id)
        trees_db = list(filter(lambda b: b["id"] != id, trees_db))
        return match

    @api.expect(tree, validate=True)
    @api.marshal_with(tree)
    def put(self, id):
        """
        Update a specific tree
        """
        match = self.find_one(id)
        if match != None:
            match.update(api.payload)
            match["id"] = id
        return match
