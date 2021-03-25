from Bilder import Bilder
from faktory import Factory
from Bilder import Product
from ColaControlFactory import ColaControlFactory
mainBilder=Bilder()
mainBilder.takeBootle(ColaControlFactory())
mainBilder.StickEtiketka(ColaControlFactory())
mainBilder.NalivGazirovki(ColaControlFactory())
mainBilder.ZakrKriwkoi(ColaControlFactory())
CompleteCocaCola=mainBilder.bildProduct()
