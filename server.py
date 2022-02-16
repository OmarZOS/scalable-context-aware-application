from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import json,os
from multiprocessing import Process, Manager

from ApplicationContext.appContext import appContext
from rabbitMQ_Implementation.listenerImplementation import rabbitMQ_Implementation

SERVING_PORT = int(os.getenv("CONTEXT_RPC_PORT"))
SERVING_HOST = str(os.getenv("CONTEXT_RPC_HOST"))

RMQ_HOST = str(os.getenv("RABBIT_MQ_HOST"))
RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))

ZOS_CONTEXT_ID = str(os.getenv("ZOS_CONTEXT_ID"))

manager = Manager()

sharedDitionary = manager.dict()

context = appContext(sharedDitionary)

# data = {
#     "user": {
#         "name": "crafter Zos",
#         "age": 23,
#         "location": "Somewhere",
#     }
# }


# context.publisher.addQueue("Context","Context1")

listener = Process(target=rabbitMQ_Implementation
                        , args=(sharedDitionary,"Context"
                        ,RMQ_USER,RMQ_PASSWORD,RMQ_HOST
                        ,"data"
                        ,ZOS_CONTEXT_ID))
listener.start()



# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer((SERVING_HOST, SERVING_PORT),
                        requestHandler=RequestHandler) as server:

    server.register_introspection_functions()

    # destined to be used by a newly recognized context instance
    def queueAdder(routeName,queueName):
        context.publisher.addQueue(routeName,queueName)
    server.register_function(queueAdder, 'addQueue') 
    
    # Setting a context variable
    def setVariable(varname,value):
        return context.set(varname,value)
    server.register_function(setVariable, 'set')
    
    # Getting a context variable
    @server.register_function(name='get')
    def getVariable(varname):
        return context.get(varname)
    # server.register_function(getVariable, )
    


    # Run the server's main loop
    server.serve_forever()