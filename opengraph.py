# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Returns the "data" dictionary of OpenGraph metadata found in HTML of given url
    """
    full_url = 'https://opengraph.lewagon.com/?url=' + url
    response = requests.get(full_url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data['data']
    print(response.status_code)
    return {}

# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.github.com"))
