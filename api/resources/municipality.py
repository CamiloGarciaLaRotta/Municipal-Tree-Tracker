from flask_restplus import Resource

from server.instance import server
from models.municipality import municipality

api = server.api

municipality_ns = api.namespace('municipalities', description='municipality related endpoints')

@municipality_ns.route('')
class MunicipalityList(Resource):
    @api.marshal_list_with(municipality)
    def get(self):
        """
        Retrieve all municipalities
        """
        # TODO
        pass

    @api.expect(municipality, validate=True)
    @api.marshal_with(municipality)
    def post(self):
        """
        Create a new municipality
        """
        # TODO
        pass

@municipality_ns.route('/<string:m_name>')
class Municipality(Resource):
    @api.marshal_with(municipality)
    def get(self, m_name):
        """
        Retrieve a specific municipality
        """
        # TODO
        pass

    @api.marshal_with(municipality)
    def delete(self, m_name):
        """
        Delete a specific municipality
        """
        # TODO
        pass

    @api.expect(municipality, validate=True)
    @api.marshal_with(municipality)
    def put(self, m_name):
        """
        Update a specific municipality
        """
        # TODO
        pass
