FROM python:3.11

RUN apt-get update

RUN apt-get install -y python3-pip

ENV OPENAI_API_KEY <key>

WORKDIR /mql

COPY requirements.txt /mql/requirements.txt

RUN pip install --upgrade -r /mql/requirements.txt

COPY .env /mql/.env

COPY ./app ./app

COPY ./scripts ./scripts

COPY ./alembic ./alembic

COPY ./alembic.ini /mql/alembic.ini

CMD ["/bin/bash", "-c", "alembic upgrade head; uvicorn app.main:app --host 0.0.0.0 --port 8000"]
