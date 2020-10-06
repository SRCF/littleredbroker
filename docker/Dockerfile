FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/code/

COPY development.txt .

RUN python -m pip install -r development.txt

COPY . .