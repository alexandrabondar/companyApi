FROM python:3.8.10-slim-buster
RUN apt-get update
RUN mkdir /flask_app

WORKDIR /flask_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /flask_app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt