from faktory import Factory
import detail
class Bilder():
    def __init__(self,faktory):
        self.faktory = faktory
        self.bootle = None

    def takeBootle(self):
        self.bootle=self.faktory.createBootle()

    def StickEtiketka(self):
        self.bootle.StickEtiketka()
    
    def NalivGazirovki(self):
        self.bootle.NalivGazirovki()

    def ZakrKriwkoi(self):
        self.bootle.ZakrKriwkoi()

    def bildProduct(self):
        #self.setParam_1(n)
        #self.setParam_2(n)
        #self.setParam_3(n)
        result=self.bootle
        return result

class Prototipe():
    def __init__(self,result):
        self.result = result
    #def copy(self):
