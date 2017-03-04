# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCliqueDevisAfficheDevis(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8080"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_clique_devis_affiche_devis(self):
        driver = self.driver
        driver.get(self.base_url + "/quotes")
        driver.find_element_by_link_text("00007").click()
        self.assertEqual("http://localhost:8080/quote/00007", driver.current_url)
        self.assertEqual("Devis 00007", driver.find_element_by_css_selector("body > p:nth-child(1)").text)
        self.assertEqual("Mozilla Inc", driver.find_element_by_css_selector("body > p:nth-child(2)").text)
        self.assertEqual("Montant: 14500.00", driver.find_element_by_css_selector("body > p:nth-child(3)").text)
        self.assertEqual("http://localhost:8080/quotes", driver.find_element_by_css_selector("body p:nth-child(5) a").get_attribute("href"))
        self.assertEqual("Liste devis", driver.find_element_by_css_selector("body p:nth-child(5) a").text)
        self.assertEqual("http://localhost:8080/valid/00007", driver.find_element_by_css_selector("body form").get_attribute("action"))
        self.assertEqual("post", driver.find_element_by_css_selector("body form").get_attribute("method"))
        self.assertEqual("date", driver.find_element_by_css_selector("body form input:nth-child(1)").get_attribute("name"))
        self.assertEqual("submit", driver.find_element_by_css_selector("body form input:nth-child(2)").get_attribute("type"))
        self.assertEqual("text", driver.find_element_by_css_selector("body form input:nth-child(1)").get_attribute("type"))

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
