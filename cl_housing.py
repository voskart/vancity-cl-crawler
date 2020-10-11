import requests
import logging
from bs4 import BeautifulSoup
import json
from mongo_client import init_connection
from mailservice import send_mail

class Housing:

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
        self.db = init_connection()

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
            apt = {'_id': id, 'link': link, 'price': price.text, 'neighborhood': neighborhood.text, 'date': date}
            # we only want to send emails if a new apt is found
            if not (db.find({'_id':id}.limit(1))):
            	send_mail(apt)
            self.db.update_one({'_id':id}, {"$set": apt}, upsert=True)

    def get_apt_number(self, soup):
        total = soup.find('span', {'class': 'totalcount'})
        logging.info('Total found apartments: %i' % int(total.text))