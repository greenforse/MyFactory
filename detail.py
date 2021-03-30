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

    def StickEtiketka(self,etiketka):
        print(f"наклеена")
        self.etiketka=etiketka
    
    def NalivGazirovki(self,gazirovka):
        print(f"залита")
        self.gazirovka= gazirovka
    
    def ZakrKriwkoi(self,kriwka):
        print(f"заркыто")
        self.kriwka=kriwka
    
class ColaBootle(Bootle):
    def __init__(self):
        self.etikitka = None
        self.kriwka = None
        self.gazirovka = None
        print("Взята Бутылка CocaColЫ")
    def StickEtiketka(self,etiketka):
        print("наклеена")
        self.etikitka=etiketka
        #print(f"наклеена{ColaEtiketka()}")
    
    def NalivGazirovki(self,gazirovka):
        print("Залита")
        self.gazirovka = gazirovka
    
    def ZakrKriwkoi(self,kriwka):
        print("закрыта")
        self.kriwka = kriwka

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