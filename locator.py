

import os
from Strategies.StrategiesImplementations.Schedulers.roundRobin import roundRobin
from rabbitMQ_Implementation.publisherImplementation import publisherImplementation

RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))

publisher = publisherImplementation(user=RMQ_USER,password=RMQ_PASSWORD)

scheduleStrategy = roundRobin()

class locator(object):
    def getPublisher():
        return publisher
    def getScheduleStrategy(type):
        # we only have one at the current time
        return scheduleStrategy
