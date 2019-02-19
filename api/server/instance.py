from flask import Flask
from flask_restplus import Api, Resource, fields
from environment.instance import environment_config

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='0.1',
            title='Tree Tracker API',
            description='API for a fictional tree management system',
            doc = environment_config["swagger-url"]
        )

    def run(self):
        self.app.run(
                debug = environment_config["debug"],
                port = environment_config["api_port"]
            )

server = Server()
