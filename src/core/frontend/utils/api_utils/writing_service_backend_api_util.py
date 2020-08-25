"""Makes remote api calls needed for the app
"""
from django.conf import settings
import requests
import logging


# test logging
def query_api(destination=None):
    url = settings.BASE_ESSAY_API_URL + destination
    try:
        response = requests.get(url, verify=False, timeout=5)
        if response.status_code == 200:
            response_object = {
                'code': 'success',
                'payload': response.json()
            }
            return response_object
        return {
            'code': 'error',
            'payload': response.status_code
        }
    except requests.exceptions.ConnectionError as e:
        logger = logging.getLogger("api-logger")
        logger.error(e)
        logger.info("connection refused for {}".format(url))
        print('Connection refused!')
        return None


def get_essay_types_for_display(essays_url='essays/'):
    """Filters through the essay api and creates a dict with
    essays and their display names

    Returns:
        dict: A dictionary containing essays with the names as the keys
        and their display names as the values
    """
    fetched_essays = query_api(essays_url)
    essays_dict = {}
    if fetched_essays and fetched_essays['code'] == 'success':
        for essay in fetched_essays['payload']:
            essays_dict[essay['essay_name']] = essay['essay_display_name']
        response_dict = {
            'code': 'success',
            'payload': essays_dict
        }
        return response_dict
    return {
        'code': 'error',
        'payload': None
    }
