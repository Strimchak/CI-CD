FROM python:latest

MAINTAINER strimchak


COPY . /home/dfo
WORKDIR /home/dfo


RUN pip install -r requirements.txt

ENTRYPOINT ['python']
CMD ['start.py']