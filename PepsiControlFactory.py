from faktory import Factory
import detail
class PepsiControlFactory(Factory):
    def createBootle(self):
        return detail.PepsiBootle()
        
    def createEtiketka(self):
        return detail.PepsiEtiketka()

    def createKriwka(self):
        return detail.PepsiKriwka()

    def createGazirovka(self):
        return detail.PepsiGazirovka()