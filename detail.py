from abc import ABCMeta, abstractmethod
class Bootle(metaclass=ABCMeta):
    @abstractmethod
    def StickEtiketka(self):
        pass
    @abstractmethod
    def NalivGazirovki(self):
        pass
    def ZakrKriwkoi(self):
        pass
class Etiketka(metaclass=ABCMeta):
    pass
class Kriwka(metaclass=ABCMeta):
    pass
class Gazirovka(metaclass=ABCMeta):
    pass

class PepsiBootle(Bootle):

    def StickEtiketka(self):
        print(f"наклеена{PepsiEtiketka}")
    
    def NalivGazirovki(self):
        print(f"залита{PepsiGazirovka()}")
    
    def ZakrKriwkoi(self):
        print(f"заркыто{PepsiKriwka()}")
    
class ColaBootle(Bootle):
    def StickEtiketka(self):
        print(f"наклеена{ColaEtiketka()}")
    
    def NalivGazirovki(self):
        print(f"залита{ColaGazirovka()}")
    
    def ZakrKriwkoi(self):
        print(f"заркыто{ColaKriwka()}")

class PepsiEtiketka(Etiketka):
    def __init__(self):
        print (" Этикетка пепси")

class ColaEtiketka(Etiketka):
    def __init__(self):
        print (" Этикетка COLA")

class PepsiKriwka(Kriwka):
    def __init__(self):
        print (" крышкой Пепси")

class ColaKriwka(Kriwka):
     def __init__(self):
        print (" крышкой Кола")

class ColaGazirovka(Gazirovka):
    def __init__(self):
        print (" газировка Cola")

class PepsiGazirovka(Gazirovka):
    def __init__(self):
        print (" газировка pepsi")