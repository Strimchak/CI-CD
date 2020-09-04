FROM python:latest

MAINTAINER strimchak

RUN pip install awscli

WORKDIR /home/dfo
COPY . /home/dfo

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "start.py" ]