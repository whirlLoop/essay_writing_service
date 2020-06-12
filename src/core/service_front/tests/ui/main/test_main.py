"""Test general site attributes such as metadata, title etc.
"""
from service_front.tests.ui.common import BaseSeleniumTestCase


class MainTestCase(BaseSeleniumTestCase):

    def setUp(self):
        super(MainTestCase, self).setUp()

    def test_website_contains_a_title(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.assertContains("Essay Service", self.driver.title)

    def test_keywords_metatag_contains_keywords(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//meta[@name='keywords']").\
            get_attribute('content')
        self.assertContains("Essay Service, Essay Writing, Essay", element)

    def test_site_is_optimized_for_mobile(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//meta[@name='viewport']").\
            get_attribute('content')
        self.assertContains("width=device-width, initial-scale=1.0", element)

    def test_site_contains_favicon(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//link[@rel='shortcut icon']").\
            get_attribute('href')
        self.assertContains("fav.png", element)

    def test_site_contains_fontawesomecss_cdn(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//link[@id='fontawesome-cdn']").\
            get_attribute('href')
        self.assertContains(
            "https://cdnjs.cloudflare.com/ajax/libs/"
            "font-awesome/5.12.0-2/css/all.min.css",
            element
        )

    def test_site_contains_materializecss_cdn(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//link[@id='materializecss-cdn']").\
            get_attribute('href')
        self.assertContains(
            "https://cdnjs.cloudflare.com/ajax/libs/"
            "materialize/1.0.0/css/materialize.min.css",
            element
        )

    def test_site_contains_materializejs_cdn(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//script[@id='materializejs-cdn']").\
            get_attribute('src')
        self.assertContains(
            "https://cdnjs.cloudflare.com/ajax/libs/"
            "materialize/1.0.0/js/materialize.min.js",
            element
        )

    def test_site_contains_jquery_cdn(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.\
            find_element_by_xpath("//script[@id='jquery-cdn']").\
            get_attribute('src')
        self.assertContains(
            "https://cdnjs.cloudflare.com/ajax/libs/"
            "jquery/3.5.1/jquery.min.js",
            element
        )

    def test_has_link_to_trigger_mobile_menu(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        element = self.driver.find_element_by_class_name('.sidenav-trigger').\
            get_attribute('data-target')
        self.assertContains(
            "mobile-navigation",
            element
        )

    def test_has_container_for_mobile_navigation_content(self):
        element = self.driver.find_element_by_class_name('.sidenav').\
            get_attribute('id')
        self.assertContains(
            "mobile-navigation",
            element
        )

    def test_site_contains_required_links(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        found_links = self.driver.find_elements_by_tag_name('a')
        links = []
        for link in found_links:
            link.upper()
            links.append(link)
        expected_links = [
            'HOW IT WORKS', 'TOP WRITERS', 'CONTACT US', 'USER REVIEWS', 'FAQS'
            'ABOUT US', 'BLOG', 'LOGIN', 'LEGAL', 'TERMS & CONDITIONS',
            'PRIVACY POLICY', 'COOKIE POLICY', 'CONFIDENTIALITY POLICY',
            'MONEY BACK GUARANTEE', 'COURSEWORK HELP', 'BUY COURSEWORK',
            'WRITE MY COURSEWORK', 'PAPER WRITING SERVICE', 'SAMPLE PAPERS',
            'THESIS WRITING SERVICE', 'BUY RESEARCH PAPER', 'RESOURCES'
            'BLOG', 'DMCA PROTECTED'
        ]
        self.assertTrue(any(link in links for link in expected_links))

    def test_home_page_link_redirects_home(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.driver.find_element_by_link_text("/").click()
        self.assertEqual(
            self.driver.current_url, '%s%s' % (self.live_server_url, '/')
            )
