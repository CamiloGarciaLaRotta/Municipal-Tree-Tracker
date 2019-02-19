from server.instance import server
import sys, os

# Need to import all resources
from resources.tree import *
from resources.park import *
from resources.city import *
from resources.municipality import *
from resources.civic_location import *

if __name__ == '__main__':
    server.run()
