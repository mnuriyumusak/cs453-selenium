# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LogInAndLogOut(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://github.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_log_in_and_log_out(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_id("login_field").clear()
        driver.find_element_by_id("login_field").send_keys("atalbayrak")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Taha9755")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_xpath("//ul[@id='user-links']/li[3]/details/summary").click()
        driver.find_element_by_link_text("Your profile").click()
        self.assertEqual("Ahmet Taha Albayrak", driver.find_element_by_xpath("//div[@id='js-pjax-container']/div/div/div[3]/h1/span").text)
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//ul[@id='user-links']/li[3]/details/summary/span").click()
        driver.find_element_by_css_selector("button.dropdown-item.dropdown-signout").click()
        self.assertEqual("Built for developers", driver.find_element_by_xpath("//h1").text)
    
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