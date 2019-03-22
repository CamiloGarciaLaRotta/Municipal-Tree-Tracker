from server.instance import server

# Need to import all resources
from resources.user import *
from resources.tree import *
from resources.park import *
from resources.city import *
from resources.municipality import *
from resources.civic_location import *
from resources.assessment import *

if __name__ == '__main__':
    server.run()
