"""Tests landing page view.
"""
from frontend.presentation.common.tests.views import BaseTestCase


class LandingPageTestCase(BaseTestCase):

    def setUp(self):
        super(LandingPageTestCase, self).setUp()
        self.root_url = self.client.get('/')
        self.other_urls = {
            'fetch_essay_types': self.client.get('/essay_types')
        }

    def test_root_url_returns_200_OK(self):
        self.assertEqual(self.root_url.status_code, 200)

    def test_correct_template_rendered(self):
        self.assertTemplateUsed(
            self.root_url, 'landing_page/index.html'
        )

    def test_correct_content_rendered_in_first_section(self):
        splash_message_title = 'Improve your grades now!'
        splash_message = (
            'No matter what kind of academic paper you need, it is simple and '
            'secure to hire an essay writer for a price you can afford at '
            'essay service. Save more time for yourself.'
        )
        self.assertInHTML(
            splash_message_title, self.root_url.content.decode()
        )
        self.assertInHTML(
            splash_message, self.root_url.content.decode()
        )

    def test_order_paper_form_contains_a_heading(self):
        heading = 'Order now'
        self.assertInHTML(
            heading, self.root_url.content.decode()
        )

    def test_order_paper_form_contains_valid_email_input(self):
        """Test that a valid name input contains a minimum of
            - is required
            - type is email
            - label
        """
        email_input = (
            '<input id="email" type="email" name="registration_email"'
        )
        self.assertIn(
            email_input, self.root_url.content.decode()
        )
        email_label = '<label for="email">Email</label>'
        self.assertInHTML(
            email_label, self.root_url.content.decode()
        )

    def test_order_form_contains_essay_type_selection_input(self):
        """Test that a valid select has at least
            - an
            - it's a select
        """
        essay_type_input = '<select name="essay_type" id="essayType"'
        self.assertIn(
            essay_type_input, self.root_url.content.decode()
        )

    def test_order_form_contains_means_to_indicate_number_of_pages(self):
        """Test that:
            - There is an input for number of pages
            - There is a means to increase the pages
            - There is a means to decrease the pages
        """
        add_pages_button = (
            '<i class="material-icons" id="removePagesBtn">remove</i>'
        )
        remove_pages_button = (
            '<i class="material-icons" id="addPagesBtn">add</i>'
        )
        pages_input = (
            '<input id="pagesInput" type="number" name="pages"'
        )
        self.assertIn(
            pages_input, self.root_url.content.decode()
        )
        self.assertInHTML(
            add_pages_button, self.root_url.content.decode()
        )
        self.assertInHTML(
            remove_pages_button, self.root_url.content.decode()
        )

    def test_order_form_contains_means_to_output_total_word_count(self):
        pages_output = (
            '<span id="totalWords">275 words</span>'
        )
        self.assertInHTML(
            pages_output, self.root_url.content.decode()
        )

    def test_order_input_form_contains_means_to_set_date_deadline(self):
        deadline_input = (
            '<input type="text" name="deadline"'
        )
        self.assertIn(
            deadline_input, self.root_url.content.decode()
        )

    def test_order_form_contains_means_to_output_order_time_left(self):
        time_left_output = '<span id="timeLeft">'
        self.assertIn(
            time_left_output, self.root_url.content.decode()
        )

    def test_order_form_has_option_to_set_time_deadline(self):
        order_time_input = '<input name="time"'
        self.assertIn(
            order_time_input, self.root_url.content.decode()
        )

    def test_order_form_has_means_to_consent_to_terms_and_conditions(self):
        terms_check_box = (
            '<input type="checkbox" checked="checked" name="terms"/>'
        )
        terms_and_conditions_urls = (
            '<span>I agree to <a href="/terms_and_conditions">Terms and '
            'conditions</a> and <a href="/privacy_policy">Privacy '
            'Policy</a></span>'
        )
        self.assertInHTML(
            terms_check_box, self.root_url.content.decode()
        )
        self.assertInHTML(
            terms_and_conditions_urls, self.root_url.content.decode()
        )

    def test_order_form_has_means_to_consent_subscriptions(self):
        subscription_check_box = (
            '<input type="checkbox" name="subscription"/>'
        )
        type_of_subscriptions = (
            '<span id="subscription">I agree to receive bonuses and '
            'promotional material</span>'
        )
        self.assertInHTML(
            subscription_check_box, self.root_url.content.decode()
        )
        self.assertInHTML(
            type_of_subscriptions, self.root_url.content.decode()
        )

    def test_order_form_contains_means_to_submit_order_info(self):
        send_button = '<button type="submit" name="action"'
        self.assertIn(
            send_button, self.root_url.content.decode()
        )

    # def test_user_can_submit_order_details(self):
    #     order_details = {
    #         "email": "test@gmail.com",
    #         "essay_type": "Thesis",
    #         "pages": 4,
    #         "date": "jul 08, 2020",
    #         "terms": True,
    #         "subscription": False
    #     }
    #     order_response = self.client.post(
    #         '/', order_details, follow=True
    #     )
    #     self.assertRedirects(order_response, '/order_confirmed', 302)
    #     self.assertTemplateUsed(
    #         order_response, 'orders/order_confirmed.html'
    #     )
    #     confirmation_message = (
    #         'Awesome test@gmail.com! we have received your paper details '
    #         'one more thing, go to your email inbox and confirm your email '
    #         'we have already sent you a link. If you can\'t find it, click '
    #         'resend below'
    #     )
    #     email_button = (
    #         '<a href="https://mail.google.com/"'
    #     )
    #     self.assertIn(
    #         confirmation_message, order_response.content.decode()
    #     )
    #     self.assertIn(
    #         email_button, order_response.content.decode()
    #     )

    # def test_user_is_notified_of_errors_in_order_form(self):
    #     order_details = {
    #         "email": "test@gmail.com",
    #         "essay_type": "Thesis",
    #         "pages": 4,
    #         "date": "jul 08, 2020",
    #         "terms": False,
    #         "subscription": False
    #     }
    #     order_response = self.client.post(
    #         '/', order_details, follow=True
    #     )
    #     self.assertTemplateNotUsed(
    #         order_response, 'orders/order_confirmed.html'
    #     )
    #     self.assertRedirects(order_response, '/', 302)
    #     message = list(order_response.context.get('messages'))[0]
    #     self.assertEqual(message.tags, 'error')
    #     s_msg = 'Please correct the errors in the form and try again.'
    #     self.assertTrue(s_msg in message.message)
    #     error_returned = (
    #         'Please accept our terms to continue'
    #     )
    #     self.assertIn(
    #         error_returned, order_response.content.decode()
    #     )

    def test_fetches_essay_types(self):
        pass
