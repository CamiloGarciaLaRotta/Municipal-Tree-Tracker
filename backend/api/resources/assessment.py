from flask import abort
from flask_restplus import Resource, reqparse

from server.instance import server, db
from models.assessment import assess_statuses, assessment
from .dao import (get_all, get_by_attr, create_single,
                  update_by_attr, delete_by_attr)

api = server.api

assess_ns = api.namespace(
    'assessment', description='tree assessment related endpoints')


@assess_ns.route('/status')
class AssessStatus(Resource):
    def get(self):
        """Retrieve all assessement status."""
        return {'status': assess_statuses}


@assess_ns.route('')
class AssessList(Resource):
    @api.marshal_list_with(assessment)
    def get(self):
        """Retrieve all assessments for a tree."""
        return get_all('assessment', db)

    @api.expect(assessment, validate=True)
    @api.marshal_with(assessment)
    def post(self):
        """Create a new assessment for a tree."""
        attrs = ['assess_date', 'assess_status', 'assess_action', 'tid', 'uid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return create_single(vals, attrs, 'assessment', db)
        except Exception as e:
            abort(400, str(e))


@assess_ns.route('/<int:tid>')
class Assess(Resource):
    @api.marshal_with(assessment)
    @api.response(404, 'Not Found')
    def get(self, tid):
        """Retrieve a specific assessment for a tree."""
        records = get_by_attr([tid], ['tid'], 'assessment', db)
        return records if records else ('Not Found', 404)

    @api.doc(params={'uid': 'Env. Scientist ID'})
    def delete(self, tid):
        """Delete a specific assessment for a tree."""
        parser = reqparse.RequestParser()
        parser.add_argument('uid', required=True,
                            help="Env. Scientist ID cannot be blank")
        args = parser.parse_args()

        ks = ['tid', 'uid']
        vs = [tid, args['uid']]
        delete_by_attr(vs, ks, 'assessment', db)

    @api.expect(assessment, validate=True)
    @api.marshal_with(assessment)
    def put(self, tid):
        """Update a specific assessment for a tree."""
        attrs = ['assess_date', 'assess_status', 'assess_action']
        vals = list(map(lambda attr: api.payload[attr], attrs))

        cond_vs = [tid, api.payload['uid']]
        cond_ks = ['tid', 'uid']

        try:
            return update_by_attr(vals, attrs, cond_vs, cond_ks,
                                  'assessment', db)
        except Exception as e:
            abort(400, str(e))
