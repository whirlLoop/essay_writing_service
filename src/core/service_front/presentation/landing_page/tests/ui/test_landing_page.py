"""Contains ui tests for the landing page."""
from service_front.tests.ui.common import BaseSeleniumTestCase


class LandingPageTestCase(BaseSeleniumTestCase):

    def setUp(self):
        super(LandingPageTestCase, self).setUp()

    def test_landing_page_url_is_root(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(self.driver.current_url,
                         '%s%s' % (self.live_server_url, '/home'))
