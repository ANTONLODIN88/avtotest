
import datetime

class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver    

    def get_current_url(self):
        """Метод проверки url"""
        get_url= self.driver.current_url
        print("current url " + get_url)

    def assert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        print(get_url)
        assert result == get_url
        print("Корректная URL")    

    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот выполнен")