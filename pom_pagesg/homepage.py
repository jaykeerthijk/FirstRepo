from library.selenium_wrapper_pom import Selenium_Wrapper
from selenium import webdriver
from time import sleep


class HomePage(Selenium_Wrapper):
    _lnk_register = ("link text", "Register")
    _lnk_login = ("link text", "Log in")

    def __init__(self, driver):
        super().__init__(driver)

    def home_click_register(self):
        self.click_element(HomePage._lnk_register)

    def home_click_login(self):
        self.click_element(HomePage._lnk_login)
