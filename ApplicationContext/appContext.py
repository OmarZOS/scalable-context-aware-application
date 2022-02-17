import json
from iContext.iContext import iContext
from locator import locator
from publishingService.publishingService import publishingService

class appContext(iContext):
    
    publisher = None #this one publishes the updates made upon context variables

    contextVariables = None
    
    def __init__ (self,contextDict):
        self.contextVariables = contextDict
        self.publisher = locator.getPublisher()
    
    def getStrategy(strategyType):
        # This function is supposed to be more sophisticated in order to make a specific choice
        return locator.getScheduleStrategy(strategyType)

    #used to set a shared object
    def set(self,varName,value,routeName="Context",validUpdate=lambda x,y:True):
        
        if validUpdate(varName,value):
            self.contextVariables[varName]=value
            self.publisher.addQueue(routeName,varName)
            dict = {}
            dict[varName]=value
            self.publisher.publish(routeName,json.dumps(dict))
            
        return True
        
    
    def get(self,varName=""):  #used to get a shared object
        if varName not in self.contextVariables.keys():
            return False
        return self.contextVariables[varName]
    
    