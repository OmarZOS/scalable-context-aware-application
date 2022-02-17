



from Strategies.AbstractStrategies.scheduleStrategy import scheduleStrategy

# This strategy has to keep a memory of the past variables and their use/call times
robinsQueues = {}
# 
class roundRobin(scheduleStrategy):
    def addElementToList(self,varName,value):
        if(varName in robinsQueues.keys()):
            if(value not in robinsQueues[varName]):
                robinsQueues[varName].extend([value])  
        else:
            robinsQueues[varName] =  [value]
    def getFrom(self,varName):
        if(varName in robinsQueues.keys()):
            val = robinsQueues[varName].pop()
            robinsQueues[varName].extend([val])
            return val
        else:
            return False
            
if __name__=="__main__":
    ruben = roundRobin()
    ruben.addElementToList("Robert",63)
    ruben.addElementToList("Roben",67)
    ruben.addElementToList("Roben",67)
    ruben.addElementToList("Roben",67)
    ruben.addElementToList("Roben",15)
    ruben.addElementToList("Roben",98)
    ruben.addElementToList("Strûdel",68)
    print(ruben.getFrom("Roben"))
    
    print(robinsQueues)