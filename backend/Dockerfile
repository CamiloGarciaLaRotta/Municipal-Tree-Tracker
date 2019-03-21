FROM python:stretch
COPY requirements.txt .
COPY api .
COPY .env .
RUN apt update -y && apt install -y gcc postgresql
RUN pip install -r requirements.txt
RUN /bin/bash -c "source .env"
CMD ["python3", "main.py"]
