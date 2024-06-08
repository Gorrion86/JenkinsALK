import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_data import LoginData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    my_account_menu_item = (By.ID, 'menu-item-100')
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    login_button = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button')
    my_account_content = (By.XPATH, '//*[@class="woocommerce-MyAccount-content"]')


def login(driver_instance):
    WebDriverWait(driver_instance, 5).until(EC.visibility_of_element_located(Locators.my_account_menu_item))
    driver_instance.find_element(*Locators.my_account_menu_item).click()
    driver_instance.find_element(*Locators.username).send_keys(LoginData.correct_username)
    driver_instance.find_element(*Locators.password).send_keys(LoginData.correct_password)
    driver_instance.find_element(*Locators.login_button).click()


def check_if_logged_in(driver_instance):
    element = WebDriverWait(driver_instance, 5).until(EC.visibility_of_element_located(Locators.my_account_content))
    return element.is_displayed()


class Test(unittest.TestCase):

    def setUp(self):

        cService = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
        self.driver = webdriver.Chrome(service=cService)
        self.driver.maximize_window()
        self.driver.get('https://tapsshop.pl/')

    def tearDown(self):
        self.driver.quit()

    def test1_login(self):
        login(self.driver)
        self.assertTrue(check_if_logged_in(self.driver))

    def test2_empty(self):
        pass
