FROM ubuntu:12.04
FROM python:2.7

COPY /. /.

RUN pip install -r requirements.txt

EXPOSE 8000
