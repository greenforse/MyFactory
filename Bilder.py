from faktory import Factory
import detail
class Bilder():
    def __init__(self,faktory):
        self.faktory = faktory
        self.bootle = None

    def takeBootle(self):
        self.bootle=self.faktory.createBootle()

    def StickEtiketka(self):
        etiketka = self.faktory.createEtiketka()
        self.bootle.StickEtiketka(etiketka)
    
    def NalivGazirovki(self):
        gazirovka=self.faktory.createGazirovka()
        self.bootle.NalivGazirovki(gazirovka)

    def ZakrKriwkoi(self):
        kriwka=self.faktory.createKriwka()
        self.bootle.ZakrKriwkoi(kriwka)

    def bildProduct(self):
        result = self.bootle.copy()
        return result

#class Prototipe():
#    def __init__(self,bootle):
#        self.bootle = bootle
#    def copy(self):
#        return self.bootle
#