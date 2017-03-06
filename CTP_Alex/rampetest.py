import unittest
from mockito import *
from rampe import Rampe

class Test_Rampe_eteindre_all(unittest.TestCase):

    def test_eteindre_rampe_toutes_les_led_etants_allumee(self):
        rampe = Rampe(mock())
        led1 = mock()
        led2 = mock()
        led3 = mock()
        tmp_rampe = [led1,led2,led3]
        rampe.setRampe(tmp_rampe)
        rampe.eteindre()

        verify(led1, times=1).eteindre()
        verify(led2, times=1).eteindre()
        verify(led3, times=1).eteindre()

class Test_Rampe_allumer_led(unittest.TestCase):

    def test_allumer_led_random(self):
        randomGenerator = mock()
        rampe = Rampe(randomGenerator)
        led1 = mock()
        led2 = mock()
        led3 = mock()
        tmp_rampe = [led1,led2,led3]
        rampe.setRampe(tmp_rampe)

        when(randomGenerator).generate().thenReturn(1)

        rampe.allumerLedRandom()

        verify(led1, times=0).allumer()
        verify(led2, times=1).allumer()
        verify(led3, times=0).allumer()

    def test_allumer_led_indice_specifique(self):
        rampe = Rampe(mock())
        led1 = mock()
        led2 = mock()
        led3 = mock()
        tmp_rampe = [led1,led2,led3]
        rampe.setRampe(tmp_rampe)

        rampe.allumer(0)

        verify(led1, times=1).allumer()
        verify(led2, times=0).allumer()
        verify(led3, times=0).allumer()
