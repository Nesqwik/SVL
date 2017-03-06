from led import LED

class Rampe:
    def __init__(self, randomGenerator):
        self.rampe = []
        self.randomGenerator = randomGenerator

    def setRampe(self,rampe):
        self.rampe = rampe

    def eteindre(self):
        for led in self.rampe:
            led.eteindre()

    def allumerLedRandom(self):
        self.allumer(self.randomGenerator.generate())

    def allumer(self, index):
        self.rampe[index].allumer()
