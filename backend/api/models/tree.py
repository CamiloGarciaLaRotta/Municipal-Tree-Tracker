from flask_restplus import fields
from server.instance import server

tree_species = ['ALDER', 'APPLE', 'ASPEN', 'BASSWOOD', 'BIRCH', 'LOCUST',
                'BUCKEYE', 'BUCKTHORN', 'CALIFORNIALAUREL', 'CATALPA',
                'CEDAR', 'CHERRY', 'CHESTNUT', 'CHINKAPIN', 'COTTONWOOD',
                'CYPRESS', 'DOGWOOD', 'DOUGLASFIR', 'ELM', 'FIR', 'FILBERT',
                'GIANTSEQUOIA', 'HAWTHORN', 'HAZEL', 'HEMLOCK', 'HONEYLOCUST',
                'HOLLY', 'HORSECHESTNUT', 'INCENSECEDAR', 'JUNIPER', 'LARCH',
                'MADRONE', 'MAPLE', 'MOUNTAINASH', 'MOUNTAINMAHOGANY', 'ASH',
                'OAK', 'OREGONMYRTLE', 'PEAR', 'PINE', 'PLUM', 'POPLAR',
                'REDCEDARARBORVITAE', 'REDWOOD', 'RUSSIANOLIVE', 'SPRUCE',
                'SWEETGUM', 'SYCAMORE', 'TANOAK', 'TRUECEDAR', 'TRUEFIR',
                'WALNUT', 'WHITECEDAR', 'WILLOW', 'YELLOWPOPLAR', 'YEW']

tree = server.api.model('Tree', {
    'tid': fields.Integer(
        description='Tree ID'),
    'species': fields.String(
        required=True,
        example='CEDAR',
        description='Scientific name',
        enum=tree_species),
    'planted_date': fields.Date(
        required=True,
        example='2015-02-26',
        description='Date when tree was planted at its current location'),
    'geog_loc': fields.String(
        required=True,
        example='(1.0,2.0)',
        description='Geographic location of the tree'),
    'mid': fields.String(
        required=True,
        example='169',
        description='ID of the municipality in which the tree is located'),
    'pid': fields.String(
        example='6',
        description='ID of the parc in which the tree is located'),
    'civid': fields.String(
        example='12',
        description='ID of the civic address in which the tree is located')
})
