# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestPython(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://urun.n11.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_2(self):
        driver = self.driver
        driver.get(self.base_url + "/cep-telefonu/apple-iphone-x-64gb-apple-turkiye-garantili-P225734508")
        Select(driver.find_element_by_id("582140183")).select_by_visible_text("Uzay Gri ( Space Gray )")
        driver.find_element_by_link_text("Sepete Ekle").click()
        driver.find_element_by_css_selector("i.icon.iconBasket").click()
        self.assertEqual(u"Apple iPhone X 64GB ( Apple Türkiye Garantili )",
                         driver.find_element_by_link_text(u"Apple iPhone X 64GB ( Apple Türkiye Garantili )").text)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()