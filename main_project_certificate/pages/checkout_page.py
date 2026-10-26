from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

class Checkout_page(Base):



    def __init__(self, driver):
        
        super().__init__(driver)
        self.driver = driver

    # Locators
    comment = "//*[@id='content_payments_tab4']/form/div[1]/div[2]/div[1]/textarea"
    aggrement_public = "//*[@id='content_payments_tab4']/form/div[1]/div[2]/div[2]/div/label"
    aggrement_payment = "//*[@id='content_payments_tab4']/form/div[1]/div[2]/div[3]/div/label/p"
    button_apply = "//*[@id='place_order_tab4']"
    text = "//*[@id='breadcrumbs_10']/div/div/span[3]"


    # Getters
    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    def get_aggrement_public(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.aggrement_public))) 
    def get_aggrement_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.aggrement_payment))) 
    def get_button_apply(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_apply)))            
    def get_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text)))  

    # Actions

    def input_comment(self, comment_text):
               
        self.get_comment().send_keys(comment_text)
        print(f"Ввводим в коммент текст {comment_text}")


    def click_aggrement_public(self):
        self.get_aggrement_public().click()
        print("Ставим галочку в оффере")
    def click_aggrement_payment(self):
        self.get_aggrement_payment().click()
        print("Ставим галочку в обработке данных")

    def click_button_apply(self):
        self.get_button_apply().click()
        print("Нажимаем Оформить заказ")

    def value_text(self):
        return self.get_text.text


    # Methods
    def checkout(self):
        self.input_comment("Тест заказа")
        self.click_aggrement_public()
        self.click_aggrement_payment()
        self.click_button_apply()
        time.sleep(5)
        self.get_screenshot()
