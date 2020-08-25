"""Contains ui tests for the landing page."""
from  time import sleep
import datetime
from selenium.webdriver.support.ui import Select
from frontend.presentation.common.tests.ui import BaseSeleniumTestCase
from frontend.presentation.common.tests.views import BaseTestCase
from selenium.webdriver.common.action_chains import ActionChains

class LandingPageTestCase(BaseSeleniumTestCase):

    def setUp(self):
        super(LandingPageTestCase, self).setUp()
        self.user_order_data = self.initialize_form_date()
        self.standard_page_word_count = 275

    def initialize_form_date(self):
        local_date = datetime.datetime.now()
        local_date = local_date + datetime.timedelta(days=3)
        return {
            "email": "testuser@gmail.com",
            "essay_type": "Essay (any type)",
            "pages": 4,
            "deadline": local_date,
            "terms": True,
            "subscription": True
        }

    def test_landing_page_has_splash_message(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        message_h2 = self.driver.find_element_by_css_selector(
            'div.splash-message h4')
        splash_message = "Improve your grades now!"
        self.assertEqual(message_h2.text, splash_message)

    def test_landing_page_has_order_essay_form(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        form_element = self.driver.find_element_by_css_selector(
            "form.order_essay_form").\
            get_attribute('method')
        assert "post" in form_element.lower()

    def fill_in_order_form(self):
        email = self.driver.find_element_by_name("email")
        email = self.driver.find_element_by_name("registration_email")
        email.send_keys(self.user_order_data['email'])
        essay_type = Select(self.driver.find_element_by_id('essayType'))
        essay_type.select_by_value("Essay (any type)")
        add_pages_button = self.driver.find_element_by_id("addPagesBtn")
        for i in range(self.user_order_data['pages'] - 1):
            add_pages_button.click()
        self.driver.find_element_by_name("deadline").\
            send_keys(str(self.user_order_data['deadline']))
        subscription_btn = self.driver.find_elements_by_id('subscription')[0]
        subscription_btn.click()

    def test_total_word_count_reflected_is_correct(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.fill_in_order_form()
        total_word_count_calculated = self.driver.\
            find_element_by_id("totalWords").text
        actual_word_count = self.standard_page_word_count * \
            self.user_order_data['pages']
        actual_word_count_string = str(actual_word_count) + " words"
        self.assertEqual(actual_word_count_string, total_word_count_calculated)

    def test_click_remove_page_button_reduces_word_count(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.fill_in_order_form()
        remove_pages_button = self.driver.find_element_by_id("removePagesBtn")
        for i in range(2):
            remove_pages_button.click()
        new_word_count = (
            self.standard_page_word_count * self.user_order_data['pages']) \
            - (self.standard_page_word_count * 2)
        total_word_count_calculated = self.driver.\
            find_element_by_id("totalWords").text
        self.assertEqual(
            str(new_word_count) + " words",
            total_word_count_calculated)
