FROM python:3.11

RUN apt-get update

RUN apt-get install -y python3-pip

ENV OPENAI_API_KEY <key>

WORKDIR /analytics

COPY requirements.txt /analytics/requirements.txt

RUN pip install --upgrade -r /analytics/requirements.txt

COPY .env /analytics/.env

COPY ./app ./app

COPY ./alembic ./alembic

COPY ./alembic.ini /analytics/alembic.ini

CMD ["/bin/bash", "-c", "alembic upgrade head; uvicorn app.main:app --host 0.0.0.0 --port 8000"]
