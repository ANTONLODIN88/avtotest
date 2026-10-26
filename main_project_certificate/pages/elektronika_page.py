from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Elektronika_page(Base):



    def __init__(self, driver):
        
        super().__init__(driver)
        self.driver = driver

    # Locators
    mobile = "//*[@id='category_products_11']/div[1]/ul/li[2]/a"


    # Getters
    def get_mobile(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mobile)))
        

    # Actions

    
    def click_mobile_button(self):
        self.get_mobile().click()
        print("Click mobile button")

    # Methods
    def elektronika(self):
        self.click_mobile_button()
        self.assert_url("https://micro-line.ru/smartfony-mobilnye-telefony/")