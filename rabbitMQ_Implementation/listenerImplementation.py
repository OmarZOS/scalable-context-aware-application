
import contextvars
import json

from uritemplate import variables

from listeningService.listeningService import listeningService
from abc import abstractmethod
import pika
from pika.exchange_type import ExchangeType

class rabbitMQ_Implementation(listeningService):
    
    identifier= 0
    contextvars=None
    
    def __init__(self,shared,routeName,user,password,hostName,exchange,identifier):#,routeName,user,password,portNumber,hostName="localhost",exchange="data"
        # self.credentials = pika.PlainCredentials(user,password)
        # print(args[4])
        self.identifier=identifier
        self.contextvars = shared
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostName))#port=portNumber, ,  credentials= self.credentials
        channel = connection.channel()
        channel.exchange_declare(exchange,  exchange_type=ExchangeType.direct)#durable=True,
        # print(args[0])
        channel.basic_consume(queue=str(routeName)+str(identifier), on_message_callback=self.receiveData, auto_ack=True)
        # print("starting consumption..")
        channel.start_consuming()
        
    def receiveData(self,ch,method,properties,body):
        # print("Ich habe gesehen was ihr wollte")
        # print("Ich bin nummer " +str(self.identifier))
        data=json.loads(body.decode())
        dateien = data["variable"]
        
        
        
        for key,value in dateien.items():
            self.contextvars[key]= value
        
         

    def transfer(self):
        # don't transfer anything!
        return


