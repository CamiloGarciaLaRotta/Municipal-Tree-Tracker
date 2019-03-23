from flask import abort
from flask_restplus import Resource, reqparse

from server.instance import server, db
from models.user import user, user_types
from .dao import (get_all, get_by_id, get_by_attr,
                  create_single_by_id, create_single, update_by_id,
                  delete_by_attr)

api = server.api

user_ns = api.namespace('users', description='user related endpoints')


@user_ns.route('/types')
class UserTypes(Resource):
    def get(self):
        """Retrieve all user types."""
        return {'types': user_types}


@user_ns.route('/login/<string:u_email>')
class Login(Resource):
    def get(self, u_email):
        """Login a resident."""
        try:
            records = get_by_attr([u_email, 'RESIDENT'], [
                'u_email', 'u_type'], 'users', db)
            return {'login': len(records) == 1}
        except Exception as e:
            abort(400, str(e))


@user_ns.route('')
class UserList(Resource):
    @api.marshal_list_with(user)
    def get(self):
        """Retrieve all users."""
        return get_all('users', db)

    @api.expect(user, validate=True)
    @api.marshal_with(user)
    def post(self):
        """Create a new user."""
        attrs = ['u_type', 'u_name', 'u_email', 'u_phone', 'civid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return create_single_by_id(vals, attrs, 'uid', 'users', db)
        except Exception as e:
            abort(400, str(e))


@user_ns.route('/<int:uid>')
class User(Resource):
    @api.marshal_with(user)
    @api.response(404, 'Not Found')
    def get(self, uid):
        """Retrieve a specific user."""
        record = get_by_id(uid, 'uid', 'users', db)
        return record if record else ('Not Found', 404)

    # def delete(self, uid):
    #     """Delete a specific user."""
    #     delete_by_attr(uid, 'uid', 'users', db)

    @api.expect(user, validate=True)
    @api.marshal_with(user)
    def put(self, uid):
        """Update a specific user."""
        attrs = ['u_type', 'u_name', 'u_email', 'u_phone', 'civid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return update_by_id(vals, attrs, uid, 'uid', 'users', db)
        except Exception as e:
            abort(400, str(e))


@user_ns.route('/reviews/<int:uid>')
class ReviewList(Resource):
    def get(self, uid):
        """Retrieve all tree reviews by an Urban Planner."""
        try:
            return get_by_attr([uid], ['uid'], 'review', db)
        except Exception as e:
            abort(400, str(e))

    @api.doc(params={'transid': 'Transaction ID'})
    def post(self, uid):
        """Create a new review by an Urban Planner."""
        parser = reqparse.RequestParser()
        parser.add_argument('transid', required=True,
                            help="Transaction ID cannot be blank")
        args = parser.parse_args()
        try:
            return create_single([args['transid'], uid],
                                 ['transid', 'uid'], 'review', db)
        except Exception as e:
            abort(400, str(e))


@user_ns.route('/reviews/<int:uid>/<int:transid>')
class Review(Resource):

    def delete(self, uid, transid):
        """Delete a specific review by an Urban Planner."""
        delete_by_attr([transid, uid], ['transid', 'uid'], 'review', db)


@user_ns.route('/orders/<int:uid>')
class OrderList(Resource):
    def get(self, uid):
        """Retrieve all tree orders of a resident."""
        try:
            return get_by_attr([uid], ['uid'], 'orders', db)
        except Exception as e:
            abort(400, str(e))

    @api.doc(params={'transid': 'Transaction ID'})
    def post(self, uid):
        """Create a new order for a resident."""
        parser = reqparse.RequestParser()
        parser.add_argument('transid', required=True,
                            help="Transaction ID cannot be blank")
        args = parser.parse_args()
        try:
            return create_single([args['transid'], uid],
                                 ['transid', 'uid'], 'orders', db)
        except Exception as e:
            abort(400, str(e))


@user_ns.route('/orders/<int:uid>/<int:transid>')
class Orders(Resource):

    def delete(self, uid, transid):
        """Delete a specific order for a resident."""
        delete_by_attr([transid, uid], ['transid', 'uid'], 'orders', db)
