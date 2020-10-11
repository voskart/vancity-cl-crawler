import requests

class Housing:

    url = None

    filters = {
        'search_distance': None,
        'postal': None,
        'max_price': None,
        'min_bedrooms': None
    }

    def __init__(self, city=None, category=None, filters=None):
        self.url = "https://{0}.craigslist.org/search/{1}".format(city, category)
        self.filters = filters

    def get_apartments(self):
        response = requests.get(self.url, params=self.filters)
        return response.content