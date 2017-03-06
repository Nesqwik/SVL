class LED:

    def __init__(self):
        '''
        Permet d'instancier une led éteinte
            >>> led = LED()
            >>> led.getStatut()
            False
        '''
        self.statut = False
        pass

    def allumer(self):
        '''
        Permet d'allumer une led sans considération de son état actuel
            >>> led = LED()
            >>> led.allumer()
            >>> led.getStatut()
            True
        '''
        self.statut = True

    def eteindre(self):
        '''
        Permet d'éteindre une led sans considération de son état actuel
            >>> led = LED()
            >>> led.eteindre()
            >>> led.getStatut()
            False
        '''
        self.statut = False

    def getStatut(self):
        '''
        Permet de connaitre l'état d'une led
            >>> led = LED()
            >>> led.getStatut()
            False
            >>> led.allumer()
            >>> led.getStatut()
            True
        '''
        return self.statut
