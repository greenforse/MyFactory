from abc import ABCMeta, abstractmethod
class Bootle(metaclass=ABCMeta):
    pass
class Etiketka(metaclass=ABCMeta):
    pass
class Kriwka(metaclass=ABCMeta):
    pass
class Gazirovka(metaclass=ABCMeta):
    pass

class PepsiBootle(Bootle):
    pass
class ColaBootle(Bootle):
    pass

class PepsiEtiketka(Etiketka):
    def __init__(self):
        print ("Наклеена Этикетка пепси")

class ColaEtiketka(Etiketka):
    def __init__(self):
        print ("Наклеена Этикетка COLA")

class PepsiKriwka(Kriwka):
    def __init__(self):
        print ("Закрыта крышкой Пепси")

class ColaKriwka(Kriwka):
     def __init__(self):
        print ("Закрыта крышкой Кола")

class ColaGazirovka(Gazirovka):
    def __init__(self):
        print ("Налита газировка Cola")

class PepsiGazirovka(Gazirovka):
    def __init__(self):
        print ("Налита газировка pepsi")