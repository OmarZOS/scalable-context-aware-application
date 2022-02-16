



from abc import ABC, abstractmethod


class iContext(ABC):
    
    routeName = "Context"
    
    @abstractmethod
    def getStrategy(args):
        pass

    @abstractmethod #used to set a shared object
    def set(args):
        pass
    
    @abstractmethod
    def get(args):  #used to get a shared object
        pass
    








