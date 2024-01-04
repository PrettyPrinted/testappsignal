FROM python:latest

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install flask==2.3.3 celery redis flask-sqlalchemy flask-wtf appsignal opentelemetry-instrumentation-flask opentelemetry-instrumentation-celery opentelemetry-instrumentation-redis

WORKDIR /app