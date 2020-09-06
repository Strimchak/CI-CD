FROM python:latest

MAINTAINER strimchak

RUN apt update -y && apt-get install -y awscli
WORKDIR /home/dfo
COPY . /home/dfo

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "start.py" ]