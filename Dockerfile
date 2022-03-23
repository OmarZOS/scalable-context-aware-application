FROM python:3.7-alpine

WORKDIR /code

RUN pip3 install -r requirements.txt

RUN apk add bind-tools 

COPY . /code


CMD ["python3", "server.py"]
