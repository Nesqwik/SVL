# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestScenarioNominalValidationDevis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_scenario_nominal_validation_devis(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Devis en attente de commandes").click()
        driver.find_element_by_link_text("00007").click()
        driver.find_element_by_name("date").clear()
        driver.find_element_by_name("date").send_keys("2222")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Accueil").click()
        driver.find_element_by_link_text(u"Commandes validées").click()
        driver.find_element_by_link_text("00007").click()
        self.assertEqual("http://localhost:8080/order/00007", driver.current_url)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
