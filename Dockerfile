FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /task

WORKDIR /task

ADD . /task/

RUN pip install -r requirements.txt