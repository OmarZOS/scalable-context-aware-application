
from abc import abstractmethod
from Strategy.strategy import Strategy

class scheduleStrategy(Strategy):
    
    @abstractmethod
    def addElementToList(self,varName,value):
        pass
    @abstractmethod
    def getFrom(self,varName):    
        pass