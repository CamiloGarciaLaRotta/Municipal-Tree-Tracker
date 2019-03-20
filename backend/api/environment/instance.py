import os
from dotenv import load_dotenv
load_dotenv()

db_user = os.environ['DB_USERNAME']
db_pass = os.environ['DB_PASSWORD']

env = os.environ.get("API_ENV", "development")

all_environments = {
    "development": {
        'db_user': db_user,
        'db_pass': db_pass,
        'db_name': 'cs421',
        'db_server': 'comp421.cs.mcgill.ca',
        "api_port": 8080,
        "debug": True,
        "swagger-url": "/api/swagger"},
    "production": {
        'db_user': db_user,
        'db_pass': db_pass,
        'db_name': 'cs421',
        'db_server': 'comp421.cs.mcgill.ca',
        "api_port": 8080,
        "debug": False,
        "swagger-url": None}
}

environment_config = all_environments[env]
