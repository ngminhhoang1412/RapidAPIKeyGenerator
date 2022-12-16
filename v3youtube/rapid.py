from time import sleep
import random
import string
from login_gmail_selenium.util.profile import ChromeProfile
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import login_gmail_selenium.util.helper as Helper
import v3youtube.delete_temp as Del_temp
import common.constants as Constant
from selenium.webdriver.common.by import By


class RapidApi:

    def __init__(self, output_file):
        self.file = output_file + '.txt'
        self.driver = None

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
        except (Exception, ValueError):
            pass

    def register(self):
        try:
            self.driver.get("https://rapidapi.com/ytdlfree/api/youtube-v31/pricing")
            selector = '#sub_btn_cnt_billingplan_bf747870-ad40-4487-b28a-2f3906f96931 > div > button > div'
            self.driver.find_element(By.CSS_SELECTOR, selector).click()
        except (Exception, ValueError):
            pass

    def create_app(self, email):
        try:
            self.driver.get("https://rapidapi.com/developer/new")
            WebDriverWait(self.driver, Constant.LOADING_TIMEOUT).until(EC.visibility_of_element_located(
                (By.ID, 'appName')))
            xpath = '//*[@id="appName"]'
            app_name = random.choices(string.ascii_lowercase, k=8)
            Helper.type_text(self.driver, xpath=xpath, text=app_name)
            key = self.get_key()
            self.write_file(key, email)
        except (Exception, ValueError):
            pass

    def get_key(self):
        show_key = "td > span > span.ant-input-suffix"
        self.driver.find_element(By.CSS_SELECTOR, show_key).click()
        key_input = "td > span > input.ant-input"
        x_rapidapi_key = self.driver.find_element(By.CSS_SELECTOR, key_input)
        return x_rapidapi_key.get_attribute('value')

    def write_file(self, key, email):
        with open(self.file, 'a') as file:
            file.write(email + ':' + key + '\n')

    def login_error(self):
        if 'auth' not in self.driver.current_url:
            return True
        else:
            return False

    def generator(self):
        f = open("accounts.txt", "r")
        for email in f:
            email = email.split(':')
            profile = ChromeProfile(email[0], email[1], email[2])
            self.driver = profile.retrieve_driver()
            profile.start()
            self.login()
            self.register()
            self.create_app(email[0])
            self.driver.quit()
            Del_temp.delete_temp()
