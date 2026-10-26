from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
from selenium.common.exceptions import StaleElementReferenceException

class Smartphony_page(Base):



    def __init__(self, driver):
        
        super().__init__(driver)
        self.driver = driver

    # Locators
    slider_from = "//*[@id='slider_61_1_left']"
    slider_to = "//*[@id='slider_61_1_right']"
    honor_brend = "//*[@id='ranges_61_11']/li[7]/label"
    huawei_brend = "//*[@id='ranges_61_11']/li[8]/label"
    samsung_brend = "//*[@id='ranges_61_11']/li[17]/label"
    tecno_brend = "//*[@id='ranges_61_11']/li[18]/label"
    xiaomi_brend = "//*[@id='ranges_61_11']/li[21]/label"
    type_smartphone = "//*[@id='ranges_61_61547']/li[1]/label"
    black_color = "//*[@id='ranges_61_61548']/li[15]/label"
    connection_5G = "//*[@id='ranges_61_61550']/li[4]/label"
    button_use = "//*[@id='product_filters_61']/div/div[30]/button"
    drop_down_popularity = "//*[@id='sw_elm_sort_fields']"
    cheeper_first = "//*[@id='elm_sort_fields']/li[1]/a"
    second_button_buy = "(//button[contains(@class, 'add-to-cart')])[2]"
    form_order = "/html/body/div[6]/div/div[2]/div[2]/a"

    # Getters
    def get_slider_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_from)))
    def get_slider_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_to)))
    def get_slider_block(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider_block))) 
    def get_honor_brend(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.honor_brend))) 
    def get_huawei_brend(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.huawei_brend)))            
    def get_samsung_brend(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.samsung_brend)))            
    def get_tecno_brend(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tecno_brend))) 
    def get_xiaomi_brend(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xiaomi_brend))) 
    def get_type_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_smartphone)))    
    def get_black_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.black_color))) 
    def get_connection_5G(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.connection_5G)))         
    def get_button_use(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_use)))
    def get_drop_down_popularity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drop_down_popularity))) 
    def get_cheeper_first(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cheeper_first))) 
    def get_second_button_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.second_button_buy))) 
    def get_form_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.form_order)))


    # Actions

    def input_slider_from(self, number_from):
        self.get_slider_from().send_keys(Keys.CONTROL + "a")
        self.get_slider_from().send_keys(Keys.DELETE)        
        self.get_slider_from().send_keys(number_from)
        print(f"Ввводим сумму от {number_from}")

    def input_slider_to(self, number_to):
        self.get_slider_to().send_keys(Keys.CONTROL + "a")
        self.get_slider_to().send_keys(Keys.DELETE)
        self.get_slider_to().send_keys(number_to)
        print(f"Ввводим сумму до {number_to}")

    def click_honor_brend(self):
        self.get_honor_brend().click()
        print("Выбираем бренд honor")
    def click_huawei_brend(self):
        self.get_huawei_brend().click()
        print("Выбираем бренд huawei")

    def scroll_block_with_mouse_wheel(self):
        scrollable_block = self.driver.find_element(By.XPATH, "//*[@id='product_filters_61']/div/div[3]")
        scroll_origin = ScrollOrigin.from_element(scrollable_block)
        actions = ActionChains(self.driver)
        actions.scroll_from_origin(scroll_origin, 0, 400).perform()        
        print("Пролистываем блок вниз")

    def scroll_page_up_with_mouse_wheel(self):
        scrollable_page = self.driver.find_element(By.XPATH, "//*[@id='tygh_main_container']/div[2]/div/div[3]")
        scroll_origin = ScrollOrigin.from_element(scrollable_page)
        actions = ActionChains(self.driver)
        actions.scroll_from_origin(scroll_origin, 0, 0).perform()        
        print("Пролистываем страницу вверх")        

    def scroll_page_down_with_mouse_wheel(self):
        scrollable_page = self.driver.find_element(By.XPATH, "//*[@id='tygh_main_container']/div[2]/div/div[3]")
        scroll_origin = ScrollOrigin.from_element(scrollable_page)
        actions = ActionChains(self.driver)
        actions.scroll_from_origin(scroll_origin, 0, 10000).perform()        
        print("Пролистываем страницу ввниз")

    def click_samsung_brend(self):
        self.get_samsung_brend().click()
        print("Выбираем бренд Samsung")

    def click_tecno_brend(self):
        self.get_tecno_brend().click()
        print("Выбираем бренд tecno")

    def click_xiaomi_brend(self):
        self.get_xiaomi_brend().click()
        print("Выбираем бренд xiaomi")

    def click_type_smartphone(self):
        self.get_type_smartphone().click()
        print("Выбираем type smartphone")

    def click_black_color(self):
        self.get_black_color().click()
        print("Выбираем black color")

    def click_connection_5G(self):
        self.get_connection_5G().click()
        print("Выбираем connection 5G")

    def click_button_use(self):
        self.get_button_use().click()
        print("Жмём кнопку Применить")

    def click_drop_down_popularity(self):
        self.get_drop_down_popularity().click()
        print("Выбираем drop down popularitye")

    def click_cheeper_first(self):
        self.get_cheeper_first().click()
        print("Выбираем Дешевле выше ")

    def click_second_button_buy(self):
        self.get_second_button_buy().click()
        print("Нажимаем купиить у второго товара в списке ")

    def click_form_order(self):
        self.get_form_order().click()
        print("Нажимаем купиить Оформить заказ ")

    # Methods
    def smartphony(self):
        try:
            self.input_slider_from("12345")
            self.input_slider_to("56789")
            self.click_honor_brend()
            self.click_huawei_brend()
            self.scroll_block_with_mouse_wheel()
            self.click_samsung_brend()
            self.click_tecno_brend()
            self.click_xiaomi_brend()
            self.click_type_smartphone()
            self.click_black_color()
            self.click_connection_5G()
            self.scroll_page_down_with_mouse_wheel()
            self.click_button_use()
            self.scroll_page_up_with_mouse_wheel()
            time.sleep(3)
            self.click_drop_down_popularity()
            self.click_cheeper_first()
            time.sleep(3)
            self.click_second_button_buy()
            self.click_form_order()
            self.assert_url("https://micro-line.ru/checkout.html")
        except StaleElementReferenceException as error:
            # Выводим ошибку в консоль
            print(f"Детали ошибки: {error.msg}")
