# FROM ubuntu:18.04
# Options: https://hub.docker.com/_/alpine
FROM python:3-slim

# RUN apt-get update
# RUN apt-get upgrade
# RUN apt-get install python3
# RUN apt-get install python3-pip

WORKDIR /usr/src/app

COPY . .

RUN pip3 install pipenv
RUN pipenv install
