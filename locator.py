

from rabbitMQ_Implementation.publisherImplementation import publisherImplementation

publisher = publisherImplementation(user="omar",password="omar")

class locator(object):
    def getPublisher():
        return publisher
