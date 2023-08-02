"""
###########################
#                         #
#   FRED's Python Magic   #
#                         #
###########################
Let the enchantment begin 🐍
"""

'''
!!!! Usefull links !!!!!
https://github.com/googleapis/google-api-python-client
https://github.com/youtube/api-samples
https://developers.google.com/youtube/v3/docs
https://developers.google.com/youtube/v3/determine_quota_cost

pip install --upgrade google-api-python-client

https://github.com/googleapis/google-cloud-python
'''

import configparser


def get_api_keys():
    config = configparser.ConfigParser()
    config.read('config.ini')

    api_keys = {}
    if 'API_KEYS' in config:
        api_keys = dict(config['API_KEYS'])

    return api_keys


# # Пример использования:
# keys = get_api_keys()
# youtube_api = keys.get('youtube_api')
#
#
# print("API Key 1:", youtube_api)

