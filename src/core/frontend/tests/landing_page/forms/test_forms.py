"""Contains tests for order form."""
from django.forms import ValidationError
from frontend.presentation.common.tests.views import BaseTestCase
from frontend.forms import CallToActionForm


class CallToActionFormTestCase(BaseTestCase):

    def setUp(self):
        super(CallToActionFormTestCase, self).setUp()
        self.form_data = {
            'email': 'test@gmail.com',
            'number_of_pages': 4,
            'date_deadline': 'Aug 24, 2020',
            'time_deadline': '4:30',
            'essay_type': 'annotated_bibliography',
            'terms_and_conditions': True,
            'bonus_and_promotions': True
        }
        self.form = CallToActionForm

    def test_validates_data(self):
        form = CallToActionForm(self.form_data)
        self.assertTrue(form.is_valid())

    def test_validates_email_format(self):
        self.form_data['email'] = 'test@gmail'
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'][0], 'The email format is invalid'
        )

    def test_returns_error_message_if_email_not_provided(self):
        self.form_data['email'] = ''
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'][0], 'Please provide an email address'
        )

    def test_returns_error_if_date_deadline_not_provided(self):
        self.form_data['date_deadline'] = ''
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        error_message = 'Please provide a deadline for your essay'
        self.assertEqual(
            form.errors['date_deadline'][0], error_message
        )

    def test_defines_time_deadline_not_required(self):
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.base_fields.get('time_deadline').required)

    def test_returns_error_if_time_deadline_format_is_wrong(self):
        self.form_data['time_deadline'] = '6hrs 30mins'
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        invalid = (
            'The time deadline provided is invalid'
            'it should be in the format (H:M) eg. 6:30'
        )
        self.assertEqual(
            form.errors['time_deadline'][0], invalid
        )

    def test_returns_error_if_invalid_date_format(self):
        self.form_data['date_deadline'] = '21-6-2020'
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        error_msg = (
            'Please provide a valid date, format should be '
            '(Month day, year) eg. Oct 25, 2006'
        )
        self.assertEqual(
            form.errors['date_deadline'][0], error_msg
        )

    def test_returns_error_if_essay_type_not_provided(self):
        self.form_data['essay_type'] = ''
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        error_msg = 'Please provide the type of essay'
        self.assertEqual(
            form.errors['essay_type'][0], error_msg
        )

    def test_validates_essay_type(self):
        self.form_data['essay_type'] = 'non_existent'
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        error_msg = 'Please select one of the choices provided'
        self.assertEqual(
            form.errors['essay_type'][0], error_msg
        )

    def test_validates_terms_and_conditions_defaults_to_true(self):
        form = CallToActionForm(self.form_data)
        self.assertTrue(form.base_fields.get('terms_and_conditions'))

    def test_returns_error_if_terms_and_conditions_not_provided(self):
        self.form_data['terms_and_conditions'] = None
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        error_msg = 'Please accepts our terms and conditions to proceed'
        self.assertEqual(
            form.errors['terms_and_conditions'][0], error_msg
        )

    def test_bonus_and_promotions_not_required(self):
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.base_fields.get('bonus_and_promotions').required)

    def test_defaults_minimum_number_of_pages_set_to_one(self):
        form = CallToActionForm(self.form_data)
        self.assertEqual(form.base_fields.get('number_of_pages').min_value, 1)

    def test_returns_error_if_number_of_pages_less_than_minimum_value(self):
        self.form_data['number_of_pages'] = 0
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        error_msg = 'Number of pages cannot be less than one'
        self.assertEqual(
            form.errors['number_of_pages'][0], error_msg
        )

    def test_returns_error_if_number_of_pages_not_provided(self):
        self.form_data['number_of_pages'] = ''
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        error_msg = 'You must provide the total number of pages'
        self.assertEqual(
            form.errors['number_of_pages'][0], error_msg
        )

    def test_valid_number_of_pages_provided(self):
        self.form_data['number_of_pages'] = 'four'
        form = CallToActionForm(self.form_data)
        self.assertFalse(form.is_valid())
        error_msg = 'Please provide a whole number for number of pages'
        self.assertEqual(
            form.errors['number_of_pages'][0], error_msg
        )
