from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cookie = "//*[@id='cookie_note']/div/button"
    cart_drop_down = "//*[@id='sw_dropdown_']"
    choose_elektronika = "//*[@id='dropdown_']/ul/li[1]/div[1]/a/span[2]"

    # Getters

    def get_cookie(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cookie)))

    def get_cart_drop_down(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_drop_down)))
    
    def get_choose_elektronika(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.choose_elektronika)))    

    # Actions
    def click_cookie(self):
        self.get_cookie().click()
        print("Click cookie")

    def click_cart_drop_down(self):
        self.get_cart_drop_down().click()
        print("Click cart drop down")

    def click_choose_elektronika(self):
        self.get_choose_elektronika().click()
        print("Click choose elektronika")

    # Methods
    def work_with_cart_drop_down(self):
        self.click_cookie()
        self.click_cart_drop_down()
        self.click_choose_elektronika()
        self.assert_url("https://micro-line.ru/elektronika/")