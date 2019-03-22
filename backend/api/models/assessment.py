from flask_restplus import fields
from server.instance import server

assess_statuses = ['HEALTHY', 'TO_CUT', 'INFESTED', 'DAMAGED']

assessment = server.api.model('Assessment', {
    'assess_date': fields.Date(
        required=True,
        example='2019-05-02',
        description='Date of the assessment yyyy-mm-dd'),
    'assess_status': fields.String(
        required=True,
        example='INFESTED',
        description='Status of the tree during the assessment'),
    'assess_action': fields.String(
        required=True,
        example='Order pesticide and schedule next assesement',
        description='Action taken during assessment'),
    'tid': fields.String(
        required=True,
        example='123',
        description='ID of the tree under assessment'),
    'uid': fields.String(
        required=True,
        example='456',
        description='ID of the env. scientist performing the assessment'),
})
