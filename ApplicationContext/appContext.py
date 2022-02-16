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
    
    def getStrategy(args):
        
        pass

    #used to set a shared object
    def set(self,varName,value,routeName="Context"):
        if self.validUpdate(varName,value):
            self.contextVariables[varName]=value
            self.publisher.addQueue(routeName,varName)
            dict = {}
            dict[varName]=value
            self.publisher.publish(routeName,json.dumps(dict))
            
        return True
        
    def validUpdate(self,varName,value):
        return True;
    
    def get(self,varName=""):  #used to get a shared object
        return self.contextVariables[varName]
    
    