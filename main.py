from Bilder import Bilder
from faktory import Factory
from Bilder import Product
from ColaControlFactory import ColaControlFactory
mainBilder=Bilder
mainBilder.setParam_1(ColaControlFactory(),createBootle())
mainBilder.setParam_2(ColaControlFactory(),createEtiketka())
mainBilder.setParam_3(ColaControlFactory(),createKriwka())
CompleteCocaCola=mainBilder.bildProduct()


