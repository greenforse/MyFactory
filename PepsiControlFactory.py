from faktory import Factory
import detail
class PepsiControlFactory(Factory):
    def createBootle(self):
        return PepsiBootle()
        
    def createEtiketka(self):
        return PepsiEtiketka()

    def createKriwka(self):
        return PepsiKriwka()