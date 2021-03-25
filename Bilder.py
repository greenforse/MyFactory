from faktory import Factory
import detail
class Product():
    def __init__(self):
        self.bootle = None
        self.etiketka = None
        self.gazirovka = None
        self.kriwka = None
class Bilder():
    def __init__(self):
        self.product= Product

    def takeBootle(self,faktory):
        self.product.bootle=faktory.createBootle()

    def StickEtiketka(self,faktory):
        self.product.etiketka=faktory.createEtiketka()
    
    def NalivGazirovki(self,faktory):
        self.product.gazirovka=faktory.createGazirovka()

    def ZakrKriwkoi(self,faktory):
        self.product.kriwka=faktory.createKriwka()

    def bildProduct(self):
        #self.setParam_1(n)
        #self.setParam_2(n)
        #self.setParam_3(n)
        result=self.product
        self.product=Product
        return result


