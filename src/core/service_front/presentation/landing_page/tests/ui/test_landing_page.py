"""Contains ui tests for the landing page."""
from selenium.webdriver.support.ui import Select
from service_front.tests.ui.common import BaseSeleniumTestCase
from service_front.tests.common import BaseTestCase


class LandingPageTestCase(BaseSeleniumTestCase):

    def setUp(self):
        super(LandingPageTestCase, self).setUp()

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

    def test_order_essay_form_has_user_email_input(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        email_element = self.driver.find_element_by_name(
            "email").get_attribute('type')
        assert 'email' in email_element

    def test_order_essay_form_has_essay_type_dropdown(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        select = Select(self.driver.find_element_by_id('essayType'))
        selected_option = select.first_selected_option
        self.assertEqual(selected_option.get_attribute("value"), "0")

    def test_order_essay_form_has_page_number_input(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        pages_element = self.driver.find_element_by_name(
            "pages").get_attribute('type')
        assert 'number' in pages_element

    def test_order_essay_form_has_deadline_input(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        deadline_element = self.driver.find_element_by_name(
            "deadline")
        self.assertIsNotNone(deadline_element)

    def test_order_essay_form_has_days_left_output(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        time_left_element = self.driver.find_element_by_id(
            "time_left")
        self.assertIsNotNone(time_left_element)

    def test_order_essay_form_has_terms_and_conditions_checkbox(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        terms_element = self.driver.find_element_by_name(
            "terms").get_attribute('checked')
        self.assertTrue(terms_element)

    def test_order_essay_form_has_email_subscription_checkbox(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        subscription_element = self.driver.find_element_by_name(
            "subscription").get_attribute('checked')
        self.assertTrue(subscription_element)
