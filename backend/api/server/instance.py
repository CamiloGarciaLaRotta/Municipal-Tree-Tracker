from flask import Flask
from flask_restplus import Api
from environment.instance import environment_config

import records


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version='0.1',
                       title='Tree Tracker API',
                       description='Fictional tree management system API',
                       doc=environment_config['swagger-url']
                       )

    def run(self):
        self.app.run(
            host='0.0.0.0',
            debug=environment_config["debug"],
            port=environment_config["api_port"]
        )


server = Server()

db_user = environment_config['db_user']
db_pass = environment_config['db_pass']
db_server = environment_config['db_server']
db_name = environment_config['db_name']

db = records.Database(f'postgres://{db_user}:{db_pass}@{db_server}/{db_name}')

# Dummy example to ensure connectivity
rows = db.query('select * from city')
print(rows[0])
##################################
