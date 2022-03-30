FROM python:3.8-alpine

WORKDIR /code

COPY . /code

RUN pip3 install -r requirements.txt

RUN apk add bind-tools 

CMD ["python3", "server.py"]
