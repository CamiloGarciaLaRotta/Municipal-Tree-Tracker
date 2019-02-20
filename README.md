# Overview

This is a simple Python API boilderplate
using [Flask](http://flask.pocoo.org/) and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).  
Persistence is achieved trhough Postgres and the [records](https://github.com/kennethreitz/records) library.

# Set Up

Clone the repo
```bash
git clone https://github.com/CamiloGarciaLaRotta/TR-API.git
cd TR-API
```

Create a virtual environment and activate it
```bash
# Python3
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

# Run locally

If you are not in the McGill campus, don't forget to connect to the [VPN](http://kb.mcgill.ca/kb/?ArticleId=1212&source=article&c=12&cid=2#tab:homeTab:crumb:8:artId:1212:src:article).

Set your ENV variables and run the API server
```bash
export DB_USERNAME=<username> && export DB_PASSWORD=<password>
python api/main.py
```

Visit the API on [http://localhost:8080/api/swagger](http://localhost:5000/api/swagger).


