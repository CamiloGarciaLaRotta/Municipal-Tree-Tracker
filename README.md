# Overview

This is a simple Python API boilderplate
using [Flask](http://flask.pocoo.org/) and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).  
Persistence is achieved trhough **[CHOOSE DB]** and the [records](https://github.com/kennethreitz/records) library.

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

```bash
PYTHON_ENV=dev python api/main.py
```

Visit the API on [http://localhost:8080/api/swagger](http://localhost:5000/api/swagger).


