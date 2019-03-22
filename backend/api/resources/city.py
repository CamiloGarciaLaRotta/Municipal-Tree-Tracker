from flask import abort
from flask_restplus import Resource, reqparse

from server.instance import server, db
from models.city import city, works_for
from .dao import (get_all, get_by_attr, get_by_id, delete_by_attr,
                  create_single_by_id, create_single, update_by_id,
                  update_by_attr)

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
            return create_single_by_id(vals, attrs, 'cid', 'city', db)
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

    # def delete(self, cid):
    #     """Delete a specific city."""
    #     delete_by_attr([cid], ['cid'], 'city', db)

    @api.expect(city, validate=True)
    @api.marshal_with(city)
    @api.response(409, 'Conflict')
    def put(self, cid):
        """Modify entry of a city."""
        attrs = ['c_name', 'c_polygon']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return update_by_id(vals, attrs, cid, 'cid', 'city', db)
        except Exception as e:
            abort(400, str(e))


@city_ns.route('/employees/<int:cid>')
class CityEmployeeList(Resource):
    @api.marshal_with(works_for)
    def get(self, cid):
        """Retrieve all employees of a city."""
        records = get_by_attr([cid], ['cid'], 'works_for', db)

        return records if records else ('Not Found', 404)

    @api.expect(works_for, validate=True)
    @api.marshal_with(works_for)
    def post(self, cid):
        """Add a new employee to a city."""
        attrs = ['start_date', 'cid', 'uid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return create_single(vals, attrs, 'works_for', db)
        except Exception as e:
            abort(400, str(e))

    @api.doc(params={'uid': 'Employee ID'})
    def delete(self, cid):
        """Delete a specific employee entry from a city."""
        parser = reqparse.RequestParser()
        parser.add_argument('uid', required=True,
                            help="Employee ID cannot be blank")
        args = parser.parse_args()
        delete_by_attr([cid, args['uid']], ['cid', 'uid'], 'works_for', db)

    @api.expect(works_for, validate=True)
    @api.marshal_with(works_for)
    def put(self, cid):
        """Modify an employee entry of a city."""
        start_date = api.payload['start_date']
        uid = api.payload['uid']
        try:
            return update_by_attr([start_date, cid, uid],
                                  ['start_date', 'cid', 'uid'], [cid, uid],
                                  ['cid', 'uid'], 'works_for', db)
        except Exception as e:
            abort(400, str(e))
