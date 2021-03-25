from Bilder import Bilder
from faktory import Factory
from Bilder import Product
from ColaControlFactory import ColaControlFactory
mainBilder=Bilder(ColaControlFactory())
mainBilder.takeBootle()
mainBilder.StickEtiketka()
mainBilder.NalivGazirovki()
mainBilder.ZakrKriwkoi()
CompleteCocaCola=mainBilder.bildProduct()
