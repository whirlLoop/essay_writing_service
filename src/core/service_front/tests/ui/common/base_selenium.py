"""Configures common ui testing attributes."""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class BaseSeleniumTestCase(StaticLiveServerTestCase):
    """Provides tools for testing the pages."""
    def setUp(self):
        """Setup initial test environment."""
        super(BaseSeleniumTestCase, self).setUp()
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        """Clear test environment.
        """
        self.driver.quit()
