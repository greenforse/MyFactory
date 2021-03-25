from abc import ABCMeta, abstractmethod
class Factory(metaclass=ABCMeta):
    @abstractmethod
    def createBootle(self,prod):
        #return bootle
        pass
    @abstractmethod
    def createEtiketka(self,prod):
        #return prod.Etiketka
        pass
    @abstractmethod
    def createKriwka(self,prod):
        #return prod.Kriwka
        pass
