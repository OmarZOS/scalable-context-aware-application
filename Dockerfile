FROM python:3.7-alpine

WORKDIR /code

# Install python/pip

RUN pip3 install pika
RUN pip3 install redis

RUN apk add bind-tools 

COPY . /code


CMD ["python3", "server.py"]