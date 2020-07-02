from django.test import TestCase, Client


class BaseTestCase(TestCase):
    """Sets up common attributes for testing the app
    """

    def setUp(self):
        """Initialise environment
        """
        super(BaseTestCase, self).setUp()
        self.client = Client()
