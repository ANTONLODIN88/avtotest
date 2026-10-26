import pytest
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import  WebDriverWait 

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.elektronika_page import Elektronika_page
from pages.smartphony_page import Smartphony_page
from pages.checkout_page import Checkout_page


def test_select_product():
    
    driver = webdriver.Chrome()

    print("Start test")

    
    

    try:
        
        login = Login_page(driver)
        login.authorization()
        mp = Main_page(driver)
        mp.work_with_cart_drop_down()
        m = Elektronika_page(driver)
        m.elektronika()
        s = Smartphony_page(driver)
        s.smartphony()
        c = Checkout_page(driver)
        c.checkout()


        time.sleep(20)

    finally:
        
        driver.quit()
        print("Браузер успешно закрыт")