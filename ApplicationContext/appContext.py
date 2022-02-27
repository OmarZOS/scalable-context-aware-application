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
    
    def getStrategy(self,strategyType):
        # This function is supposed to be more sophisticated in order to make a specific choice
        return locator.getScheduleStrategy(strategyType)

    #used to set a shared object
    def set(self,varName,value,strategy="schedule",routeName="Context",validUpdate=lambda x,y:True):
        
        if validUpdate(varName,value):
            self.contextVariables[varName]=value
            # self.publisher.addQueue(routeName,varName)
            dict = {}
            varDict = {}
            varDict[varName] = value
            dict["variable"] = varDict
            
            self.getStrategy(strategy).addElementToList(varName,value)
            try:
                self.publisher.publish(routeName,json.dumps(dict))
            except print(0):
                pass
            
        return True
        
    
    def get(self,varName="",put_at_end=True):  #used to get a shared object
        if varName not in self.contextVariables.keys():
            return False
        return self.getStrategy("schedule").getFrom(varName,put_at_end)