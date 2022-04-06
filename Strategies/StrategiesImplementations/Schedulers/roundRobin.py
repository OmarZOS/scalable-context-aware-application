from Strategies.AbstractStrategies.scheduleStrategy import scheduleStrategy
from redis_client import redisClient

# This strategy has to keep a memory of the past variables and their use/call times
# In order to keep the consistency of multiple contexts, the use of a key value cache server was recommended
from redis_client import redisClient


robinsQueues = {}
# 
class roundRobin(scheduleStrategy):
    cacheServer = redisClient()
    def addElementToList(self,varName,value):
        localList=[]
        try :
            localList=robinsQueues[varName]
        except:
            localList=[]
         
        remoteList = self.cacheServer.getValue(varName)
        if not isinstance(remoteList, list):
            remoteList = []
        
        robinsQueues[varName] = self.integrateLists(remoteList,localList)
        
        #get the latest state of the queue
        robinsQueues[varName] = self.integrateLists(remoteList,localList)
        
        if(varName in robinsQueues.keys()):
            if(value not in robinsQueues[varName]):
                robinsQueues[varName].extend([value])
                self.cacheServer.setValue(varName,robinsQueues[varName])  
        else:
            robinsQueues[varName] =  [value]
            
    def getFrom(self,varName,put_at_end= True):
        # localList=[]
        # try :
        #    localList=robinsQueues[varName]
        # except:
        #     pass
         
        # remoteList = self.cacheClient.getValue(varName)
        # if not isinstance(remoteList, list):
        #     remoteList = []
        
        # robinsQueues[varName] = self.integrateLists(localList,remoteList)
        
        #get the latest state of the queue
        # robinsQueues[varName] = self.integrateLists(remoteList,localList)
        # print(robinsQueues)
        
        if(varName in robinsQueues.keys()):
            val = robinsQueues[varName].pop(0)
            if put_at_end :
                robinsQueues[varName].extend([val])
            self.cacheServer.setValue(varName,robinsQueues[varName])  
            return val
        else:
            return False
        
    # future work: fault tolerance, multi agent redis modification
    def integrateLists(self,list1,list2):
        in_first = set(list1)
        in_second = set(list2)
        in_second_but_not_in_first = in_second - in_first
        return list1 + list(in_second_but_not_in_first)


        
            
if __name__=="__main__":
    ruben = roundRobin()
    ruben.addElementToList("Robert",lambda x,y:True)
    ruben.addElementToList("Roben",67)
    ruben.addElementToList("Roben",67)
    ruben.addElementToList("Roben",67)
    ruben.addElementToList("Roben",15)
    ruben.addElementToList("Roben",98)
    ruben.addElementToList("Strûdel",68)
    print(ruben.getFrom("Roben"))
    
    print(robinsQueues)