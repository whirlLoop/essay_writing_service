"""Test general site attributes such as metadata, title etc.
"""
from frontend.presentation.common.tests.ui import BaseSeleniumTestCase


class MainTestCase(BaseSeleniumTestCase):

    def setUp(self):
        super(MainTestCase, self).setUp()

    def test_website_contains_a_title(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        assert "Essay Service" in self.driver.title

    def test_keywords_metatag_contains_keywords(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//meta[@name='keywords']").\
            get_attribute('content')
        assert "Essay Service, Essay Writing, Essay" in element

    def test_site_is_optimized_for_mobile(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//meta[@name='viewport']").\
            get_attribute('content')
        assert "width=device-width, initial-scale=1.0" in element

    def test_site_contains_favicon(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//link[@rel='shortcut icon']").\
            get_attribute('href')
        assert "logo.jpg" in element

    def test_site_contains_fontawesomecss_cdn(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//link[@id='fontawesome-cdn']").\
            get_attribute('href')
        assert "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.0-2/css/all.min.css" in element

    def test_site_contains_materializecss_cdn(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//link[@id='materializecss-cdn']").\
            get_attribute('href')
        assert "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" in element

    def test_site_contains_materializejs_cdn(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//script[@id='materializejs-cdn']").\
            get_attribute('src')
        assert "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js" in element

    def test_site_contains_jquery_cdn(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//script[@id='jquery-cdn']").\
            get_attribute('src')
        assert "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" in element

    def test_has_link_to_trigger_mobile_menu(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.find_element_by_class_name('sidenav-trigger').\
            get_attribute('data-target')
        assert "mobile-navigation" in element

    def test_has_container_for_mobile_navigation_content(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.find_element_by_class_name('sidenav').\
            get_attribute('id')
        assert "mobile-navigation" in element

    def test_site_contains_required_links(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        found_links = self.driver.find_elements_by_tag_name('a')
        links = []
        for link in found_links:
            links.append(link.text.upper())
        expected_links = [
            'HOW IT WORKS', 'TOP WRITERS', 'CONTACT US', 'USER REVIEWS',
            'FAQS', 'ABOUT US', 'BLOG', 'TERMS & CONDITIONS',
            'PRIVACY POLICY', 'COOKIE POLICY', 'CONFIDENTIALITY POLICY',
            'MONEY BACK GUARANTEE', 'COURSEWORK HELP', 'BUY COURSEWORK',
            'WRITE MY COURSEWORK', 'PAPER WRITING SERVICE', 'SAMPLE PAPERS',
            'THESIS WRITING SERVICE', 'BUY RESEARCH PAPER', 'RESOURCES',
            'BLOG', 'T&C'
        ]
        self.assertTrue(all(link in links for link in expected_links))

    def test_home_page_link_redirects_home(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.driver.find_element_by_class_name("brand-logo").click()
        self.assertEqual(
            self.driver.current_url, '%s%s' % (self.live_server_url, '/')
            )

    def test_base_template_has_login_form(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.find_element_by_class_name('login-form').\
            get_attribute('action')
        assert "/login" in element
