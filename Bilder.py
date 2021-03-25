from faktory import Factory
import detail
class Product():
    def __init__(self):
        self.bootle = None
        self.etiketka = None
        self.gazirovka = None
        self.kriwka = None
class Bilder():
    def __init__(self,faktory):
        self.faktory = faktory
        self.product = Product

    def takeBootle(self):
        self.product.bootle=self.faktory.createBootle()

    def StickEtiketka(self):
        self.product.etiketka=self.faktory.createEtiketka()
        self.product.bootle.StickEtiketka()
    
    def NalivGazirovki(self):
        self.product.gazirovka=self.faktory.createGazirovka()
        self.product.bootle.NalivGazirovki()

    def ZakrKriwkoi(self):
        self.product.kriwka=self.faktory.createKriwka()
        self.product.bootle.ZakrKriwkoi()

    def bildProduct(self):
        #self.setParam_1(n)
        #self.setParam_2(n)
        #self.setParam_3(n)
        result=self.product
        self.product=Product
        return result


