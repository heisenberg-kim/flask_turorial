FROM python:latest

RUN pip install flask

WORKDIR /app

COPY flask_tutorial /app


