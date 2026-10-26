from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):

    url = "https://micro-line.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    drop_down = "//*[@id='sw_dropdown_1169']/a"
    enter_button = "//*[@id='account_info_1169']/div[2]/a[1]"
    user_name = "//*[@id='login_popup1169']"
    password = "//*[@id='psw_popup1169']"
    accept_terms = "//*[@id='login_block1169']/div/div/form/div[4]/label"
    login_button = "//*[@id='login_block1169']/div/div/form/div[5]/div[1]/button"
    

    # Getters

    def get_drop_down(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.drop_down)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
        
    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    
    def get_accept_terms(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.accept_terms)))
        
    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

      

    # Actions
    def click_drop_down(self):
        self.get_drop_down().click()
        print("Click drop down")  

    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click drop down") 

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_accept_terms(self):
        self.get_accept_terms().click()
        print("Click accept button")

    
    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")



    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_drop_down()
        self.click_enter_button()
        self.input_user_name("xphoenix@gmail.com")
        self.input_password("LGQx9Jfqx88mNvU")
        self.click_accept_terms()
        self.click_login_button()
        