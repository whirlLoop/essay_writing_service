"""Contains landing page forms.
"""
from django import forms
from frontend.utils import get_essay_types_for_display


class CallToActionForm(forms.Form):
    """This form initiates user interaction. It collects
    their email and prompts them to make an order

    Args:
        forms (class): describes the logical structure of an object
    """
    error_messages = {
        'email': {
            'required': 'Please provide an email address',
            'invalid': 'The email format is invalid'
        },
        'number_of_pages': {
            'required': 'You must provide the total number of pages',
            'invalid': 'Please provide a whole number for number of pages',
            'min_value': 'Number of pages cannot be less than one'
        },
        'date_deadline': {
            'required': 'Please provide a deadline for your essay',
            'invalid': (
                'Please provide a valid date, format should be '
                '(Month day, year) eg. Oct 25, 2006'
            )
        },
        'time_deadline': {
            'invalid': (
                'The time deadline provided is invalid'
                'it should be in the format (H:M) eg. 6:30'
            ),
        },
        'essay_type': {
            'required': 'Please provide the type of essay',
            'invalid_choice': 'Please select one of the choices provided'
        },
        'terms_and_conditions': {
            'required': 'Please accepts our terms and conditions to proceed'
        }
    }
    essays = get_essay_types_for_display()
    CHOICES = ()
    if essays['code'] == 'success':
        CHOICES = tuple((k, v) for k, v in essays['payload'].items())
    email = forms.EmailField(error_messages=error_messages['email'])
    number_of_pages = forms.IntegerField(
        min_value=1, error_messages=error_messages['number_of_pages']
    )
    date_deadline = forms.DateField(
        input_formats=['%b %d, %Y'],
        error_messages=error_messages['date_deadline']
    )
    time_deadline = forms.TimeField(
        required=False,
        input_formats=['%H:%M'],
        error_messages=error_messages['time_deadline']
    )
    essay_type = forms.ChoiceField(
        choices=CHOICES,
        error_messages=error_messages['essay_type']
    )
    terms_and_conditions = forms.BooleanField(
        error_messages=error_messages['terms_and_conditions']
    )
    bonus_and_promotions = forms.BooleanField(required=False)
