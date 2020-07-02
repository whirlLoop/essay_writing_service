"""Configures common ui testing attributes."""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BaseSeleniumTestCase(StaticLiveServerTestCase):
    """Provides tools for testing the pages."""
    def setUp(self):
        """Setup initial test environment."""
        super(BaseSeleniumTestCase, self).setUp()
        chrome_options = self.setup_chrome_options_for_local_testing()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(30)

    def setup_chrome_options_for_local_testing(self):
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')
        return chrome_options

    def setup_chrome_options_for_docker(self):
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        return chrome_options

    def tearDown(self):
        """Clear test environment.
        """
        self.driver.quit()
