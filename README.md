# Overview

This is a simple Python API boilderplate
using [Flask](http://flask.pocoo.org/) and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).  
Persistence is achieved through Postgres and the [records](https://github.com/kennethreitz/records) library.


# How to run locally

Once deployed locally, you can visit the on [http://localhost:8080/api/swagger](http://localhost:5000/api/swagger).

### Prerequisites
 - If you are not in the McGill campus, don't forget to connect to the [VPN](http://kb.mcgill.ca/kb/?ArticleId=1212&source=article&c=12&cid=2#tab:homeTab:crumb:8:artId:1212:src:article)
 - Clone the repo
 
    ```bash
    git clone https://github.com/CamiloGarciaLaRotta/TR-API.git
    cd TR-API
   ```
 - Create a `.env` file in the base directory of the repo with the following:
 
    ```bash
    DB_USERNAME=<your_username>
    DB_PASSWORD=<your_password>
    ```

### Through Docker

Build the Docker image from the base directory

```bash
docker build --rm -f "Dockerfile" -t tr-api:latest .
```

Run the container and map its localhost with your localhost
```bash
docker run --rm -p 127.0.0.1:8080:8080 -it tr-api:latest
```

### Directly on your machine

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

Run the API server

```bash
python api/main.py
```
