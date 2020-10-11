import requests
import logging
from bs4 import BeautifulSoup

class Housing:

    results = {}

    filters = {
        'search_distance': None,
        'postal': None,
        'max_price': None,
        'min_bedrooms': None
    }

    def __init__(self, city=None, category=None, filters=None):
        logging.basicConfig(level=logging.INFO)
        self.url = "https://{0}.craigslist.org/search/{1}".format(city, category)
        self.filters = filters

    def get_apartments(self):
        response = requests.get(self.url, params=self.filters)
        soup = BeautifulSoup(response.content, 'html.parser')
        # find all results
        rows = soup.find_all('li', {'class': 'result-row'})
        self.process_rows(rows)
        self.get_apt_number(soup)

    def process_rows(self, rows):
    	apt = None
    	for row in rows:
    		id = row.attrs['data-pid']
    		link = row.find('a')['href']
    		price = row.find('span', {'class': 'result-price'})
    		neighborhood = row.find('span', {'class': 'result-hood'})
    		date = row.find('time')['datetime']
    		self.results[id] = {'link': link, 'price': price.text, 'neighborhood': neighborhood.text, 'date': date}

    def get_apt_number(self, soup):
        total = soup.find('span', {'class': 'totalcount'})
        logging.info('Total found apartments: %i' % int(total.text))