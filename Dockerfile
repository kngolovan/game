FROM python:3.9-alpine

RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev

WORKDIR /practice

COPY app ./app
COPY migrations ./migrations
COPY scripts ./scripts
COPY alembic.ini setup.py wsgi.py ./

RUN pip install -e .

RUN chmod +x scripts/apply-migrations.sh
ENTRYPOINT ["./scripts/apply-migrations.sh"]

CMD ["gunicorn", "wsgi:app"]
