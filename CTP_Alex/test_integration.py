import unittest
from mockito import *
from led import LED
from rampe import Rampe

class Test_Rampe_allumer_led(unittest.TestCase):

    def test_allumer_led_random(self):
        randomGenerator = mock()
        rampe = Rampe(randomGenerator)
        led1 = LED()
        led2 = LED()
        led3 = LED()
        tmp_rampe = [led1,led2,led3]
        rampe.setRampe(tmp_rampe)

        when(randomGenerator).generate().thenReturn(1)

        rampe.allumerLedRandom()

        self.assertTrue(led2.getStatut())
        self.assertFalse(led1.getStatut())
        self.assertFalse(led3.getStatut())
