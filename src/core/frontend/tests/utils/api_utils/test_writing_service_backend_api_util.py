"""Tests api utils
"""
from unittest import TestCase
from frontend.utils import query_api, get_essay_types_for_display


class WritingServiceBackendApiTestCase(TestCase):

    def setUp(self):
        self.get_essay_types_response = query_api('essays/')
        self.get_essay_types_for_display_response = get_essay_types_for_display()

    def test_success_code_if_query_api_request_success(self):
        self.assertEqual(self.get_essay_types_response['code'], 'success')

    def test_returns_dict_object_on_get_essays_success(self):
        self.assertIsInstance(self.get_essay_types_response, dict)

    def test_returns_essay_payload_as_list_if_request_successful(self):
        self.assertIsInstance(self.get_essay_types_response['payload'], list)

    def test_returns_error_code_if_request_fail(self):
        response = query_api('essayss/')
        self.assertEqual(response['code'], 'error')

    def test_returns_api_response_code_if_request_fail(self):
        response = query_api('essayss/')
        self.assertEqual(response['payload'], 404)

    def test_get_essay_types_function_logs_errors_on_failure(self):
        pass

    def test_get_essay_types_for_display_returns_essay_dict_as_payload_on_success(self):
        self.assertIsInstance(self.get_essay_types_for_display_response['payload'], dict)

    def test_returns_dict_object_on_get_essays_for_display_success(self):
        self.assertIsInstance(self.get_essay_types_for_display_response, dict)

    def test_success_code_if_get_essay_types_for_display_request_success(self):
        self.assertEqual(self.get_essay_types_for_display_response['code'], 'success')

    def test_error_code_if_get_essay_types_for_display_request_fail(self):
        get_essay_types_for_display_response = get_essay_types_for_display(essays_url='essayss')
        self.assertEqual(get_essay_types_for_display_response['code'], 'error')