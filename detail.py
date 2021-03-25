from abc import ABCMeta, abstractmethod
class Bootle(metaclass=ABCMeta):
    @abstractmethod
    def call(self):
        pass


class Etiketka(metaclass=ABCMeta):
    @abstractmethod
    def call(self):
        pass

class Kriwka(metaclass=ABCMeta):
   @abstractmethod
   def call(self):
       pass

class PepsiBootle(Bootle):
    def call(self):
        pass

class ColaBootle(Bootle):
    def call(self):
        pass

class PepsiEtikentka(Etiketka):
    def call(self):
        pass

class ColaEtikentka(Etiketka):
    def call(self):
        pass  

class PepsiKriwka(Kriwka):
    def call(self):
        pass

class ColaKriwka(Kriwka):
    def call(self):
        pass