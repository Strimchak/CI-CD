FROM python:latest

MAINTAINER strimchak

WORKDIR /home/dfo
COPY . /home/dfo

RUN pip install -r requirements.txt

ENTRYPOINT [ "start.py" ]