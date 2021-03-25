from faktory import Factory
import detail
class Product():
    def __init__(self):
        self.param_1
        self.param_2
        self.param_3

class Bilder():
    def __init__(self):
        self.product= Product()

    def setParam_1(self,faktory,detail):
        self.product.param_1=faktory.detail()

    def setParam_2(self,faktory,detail):
        self.product.param_2=faktory.detail()
    
    def setParam_3(self,faktory,detail):
        self.product.param_3=faktory.detail()

    def bildProduct(self,n):
        #self.setParam_1(n)
        #self.setParam_2(n)
        #self.setParam_3(n)
        result=self.product
        self.product=Product
        return result


