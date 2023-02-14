import os
from login_gmail_selenium.util.profile import ChromeProfile
import common.constants as Constant
from fake_headers import Headers
from v3youtube.rapid import RapidApi
import login_gmail_selenium.common as LGS_common


class Flow:
    def __init__(self, position, services):
        self.node = None
        self.driver = None
        self.position = position
        self.gmail = None
        self.proxy = None
        self.services = services
        self.get_resource()

    def setup_proxy(self):
        header = Headers(
            browser="chrome",
            os=Constant.osname,
            headers=False
        ).generate()
        agent = header['User-Agent']
        self.setup_chrome_profile()

    def setup_chrome_profile(self):
        proxy_folder = os.path.join(LGS_common.constant.PROXY_FOLDER, f'proxy_auth')
        profile = ChromeProfile(self.gmail[0], self.gmail[1], self.gmail[2], auth_type='private',
                                path=None, prox=self.proxy, prox_type='http', proxy_folder=proxy_folder,
                                false_email_callback=self.false_email_callback)
        driver = profile.retrieve_driver()
        self.driver = driver
        profile.start()
        rapid = RapidApi(self.services, driver=driver, email=self.gmail[0])
        rapid.generate_key()

    def generate_rapid_key(self):
        self.setup_proxy()

    def get_resource(self):
        position = self.position
        resource = Constant.resources[position]
        current_proxy = resource["proxy"]
        gmail = resource["email"]
        self.gmail = gmail
        proxy = current_proxy
        self.proxy = proxy

    def false_email_callback(self, email, password, backup_email, error):
        pass
