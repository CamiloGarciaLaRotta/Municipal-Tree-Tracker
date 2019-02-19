from flask_restplus import fields
from server.instance import server

tree = server.api.model('Tree', {
    'id': fields.Integer(description='Id'),
    'species': fields.String(required=True, example='CEDAR', description='Scientific name', enum=['ALDER', 'APPLE', 'ASH', 'ASPEN', 'BASSWOOD', 'BIRCH', 'BUCKEYE', 'BUCKTHORN', 'CALIFORNIALAUREL', 'CATALPA', 'CEDAR', 'CHERRY', 'CHESTNUT', 'CHINKAPIN', 'COTTONWOOD', 'CYPRESS', 'DOGWOOD', 'DOUGLASFIR', 'ELM', 'FIR', 'FILBERT', 'GIANTSEQUOIA', 'HAWTHORN', 'HAZEL', 'HEMLOCK', 'HONEYLOCUST', 'HOLLY', 'HORSECHESTNUT', 'INCENSECEDAR', 'JUNIPER', 'LARCH', 'LOCUST', 'MADRONE', 'MAPLE', 'MOUNTAINASH', 'MOUNTAINMAHOGANY', 'OAK', 'OREGONMYRTLE', 'PEAR', 'PINE', 'PLUM', 'POPLAR', 'REDCEDARARBORVITAE', 'REDWOOD', 'RUSSIANOLIVE', 'SPRUCE', 'SWEETGUM', 'SYCAMORE', 'TANOAK', 'TRUECEDAR', 'TRUEFIR', 'WALNUT', 'WHITECEDAR', 'WILLOW', 'YELLOWPOPLAR', 'YEW']),
    'planted_on': fields.Date(required=True, example='2015-02-26', description='Date when tree was planted at its current location'),
    'lon': fields.String(required=True, example='23.4E', description='Longitude of the tree'),
    'lat': fields.String(required=True, example='23.4N', description='Latitude of the tree'),
    'm_name': fields.String(required=True, example='St-Henri', description='Municipality in which the tree is located'),
    'p_name': fields.String(example='Parc Angrignon', description='Parc in which the tree is located')
})
