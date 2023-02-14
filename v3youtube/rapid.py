import os
from time import sleep
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import login_gmail_selenium.util.helper as Helper
import v3youtube.helper as help_rapid
import common.constants as Constant
from selenium.webdriver.common.by import By
from common.log import log_error


class RapidApi:

    def __init__(self, services, driver, email):
        self.driver = driver
        self.error = None
        self.proxy = None
        self.gmail = email
        self.services = services

    def login(self):
        try:
            self.driver.get('https://accounts.google.com/'
                            'o/oauth2/v2/auth/oauthchooseaccount?response_type=code&'
                            'redirect_uri=https%3A%2F%2Frapidapi.com%2Fauthentication%2Fgoogle%2Fcallback&'
                            'scope=email%20profile&state=%223%22&'
                            'client_id=991879354912-toqgimi10brc511d062b8e8ru7hfa8go.apps.googleusercontent.com&'
                            'service=lso&o2v=2&flowName=GeneralOAuthFlow')
            choose_account = '.JDAKTe > div'
            self.driver.find_element(By.CSS_SELECTOR, choose_account).click()
            sleep(Constant.SHORT_WAIT)
        except (Exception, ValueError) as err:
            log_error(err)

    def register(self):
        for service in self.services:
            try:
                self.driver.get(service)
                self.driver.execute_script("document.getElementsByClassName('primary')[1].click()")
            except (Exception, ValueError) as err:
                log_error(err)

    def create_app(self, email):
        try:
            self.driver.get("https://rapidapi.com/developer/new")
            WebDriverWait(self.driver, Constant.LOADING_TIMEOUT).until(EC.visibility_of_element_located(
                (By.ID, 'appName')))
            xpath = '//*[@id="appName"]'
            app_name = random.choices(string.ascii_lowercase, k=8)
            Helper.type_text(self.driver, xpath=xpath, text=app_name)
            key = self.get_key()
            help_rapid.write_file('rapid_key.txt', content=key, email=email)
        except (Exception, ValueError) as err:
            log_error(err)
            self.error = 'login_google_fail'
            help_rapid.write_file(file='error_email.txt', content=self.error, email=email)
            self.error = None

    def get_key(self):
        show_key = "td > span > span.ant-input-suffix"
        self.driver.find_element(By.CSS_SELECTOR, show_key).click()
        key_input = "td > span > input.ant-input"
        x_rapidapi_key = self.driver.find_element(By.CSS_SELECTOR, key_input)
        return x_rapidapi_key.get_attribute('value')

    def generate_key(self):
        self.login()
        self.register()
        self.create_app(self.gmail)
        self.driver.quit()
        help_rapid.delete_temp()
