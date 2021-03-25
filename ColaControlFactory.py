from faktory import Factory
from detail import ColaBootle , ColaEtiketka , ColaKriwka
class ColaControlFactory(Factory):
    def createBootle(self):
        return ColaBootle()

    def createEtiketka(self):
        return ColaEtiketka()

    def createKriwka(self):
        return ColaKriwka()
