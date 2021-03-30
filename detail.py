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
    def __init__(self):
        self.etiketka=None
        self.kriwka=None
        self.gazirovka= None
        print("Взята бутылочка PEPSI")

    def StickEtiketka(self):
        print(f"наклеена",end="")
        self.etiketka=PepsiEtiketka()
    
    def NalivGazirovki(self):
        print(f"залита",end="")
        self.gazirovka= PepsiGazirovka()
    
    def ZakrKriwkoi(self):
        print(f"заркыто",end="")
        self.kriwka=PepsiKriwka()
    
class ColaBootle(Bootle):
    def __init__(self):
        self.etikitka = None
        self.kriwka = None
        self.gazirovka = None
        print("Взята Бутылка CocaColЫ")
    def StickEtiketka(self):
        print("наклеена",end="")
        self.etikitka=ColaEtiketka()
        #print(f"наклеена{ColaEtiketka()}")
    
    def NalivGazirovki(self):
        print("Залита",end="")
        self.gazirovka = ColaGazirovka()
    
    def ZakrKriwkoi(self):
        print("закрыта",end="")
        self.kriwka = ColaKriwka()

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