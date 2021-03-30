from Bilder import Bilder
from faktory import Factory
#from Bilder import Product
from ColaControlFactory import ColaControlFactory
from PepsiControlFactory import PepsiControlFactory
mainBilder=Bilder(PepsiControlFactory())
mainBilder.takeBootle()
mainBilder.StickEtiketka()
mainBilder.NalivGazirovki()
mainBilder.ZakrKriwkoi()
CompleteCocaCola=mainBilder.bildProduct()