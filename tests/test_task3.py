from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class test_yandex_enter(unittest.TestCase):

    def setUp(self) -> None:
        self.username = 'user'
        self.password = 'password'
        self.driver = webdriver.Chrome()

    def test_selenium(self):

        self.driver.get("https://passport.yandex.ru/auth")

        # ищем поле логина
        login_input = self.driver.find_element(By.NAME, "login")
        login_input.send_keys(self.username)
        login_input.send_keys(Keys.RETURN)

        time.sleep(2)  # Ждем, чтобы загрузилась следующая страница

        # ищем поле пароля
        password_input = self.driver.find_element(By.NAME, "passwd")
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(5)  # Ждем, чтобы проверить успешный вход

        flag = False
        if "Добро пожаловать" in self.driver.page_source:
             flag = True
        else:
             flag = False

        self.assertEqual(flag, True)
        self.driver.quit()  # Закрываем браузер