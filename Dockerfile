FROM python:3.9-alpine

RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev

WORKDIR /practice

COPY app ./app
COPY migrations ./migrations
COPY alembic.ini setup.py ./

RUN pip install -e .
