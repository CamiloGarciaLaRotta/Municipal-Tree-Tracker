FROM python:3.6-alpine as base

FROM base as builder

RUN mkdir /install
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

LABEL Name=tr-api Version=0.0.1
EXPOSE 8080

COPY --from=builder /install /usr/local
COPY api /api
RUN apk --no-cache add libpq
WORKDIR /api
CMD ["python3", "main.py"]
