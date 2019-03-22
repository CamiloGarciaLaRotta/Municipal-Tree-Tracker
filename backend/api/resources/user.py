from flask import abort
from flask_restplus import Resource

from server.instance import server, db
from models.user import user, user_types
from .dao import get_all, get_by_id, create_single_by_id, update_by_id

api = server.api

user_ns = api.namespace('users', description='user related endpoints')


@user_ns.route('/types')
class UserTypes(Resource):
    def get(self):
        """Retrieve all user types."""
        return {'types': user_types}


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
