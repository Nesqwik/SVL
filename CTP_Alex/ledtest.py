import unittest
from led import LED

class Test_LED_allumer_led(unittest.TestCase):

    def test_allumer_led_eteinte(self):
        led = LED()
        led.statut = False
        led.allumer()
        self.assertTrue(led.getStatut())

    def test_allumer_led_allumee(self):
        led = LED()
        led.statut = True
        led.allumer()
        self.assertTrue(led.getStatut())

class Test_LED_eteindre_led(unittest.TestCase):

    def test_eteindre_led_allumee(self):
        led = LED()
        led.statut = True
        led.eteindre()
        self.assertFalse(led.getStatut())

    def test_eteindre_led_eteinte(self):
        led = LED()
        led.statut = False
        led.eteindre()
        self.assertFalse(led.getStatut())
