from mailservice import send_mail
from cl_housing import Housing
import logging
from mongo_client import init_connection


def main():
    apt_van = Housing(city='vancouver', category='apa', filters={'max_price': 1800, 'min_bedrooms': 2, 'search_distance': 6, 'postal':'V6H1T4', 'postedToday':1})
    apt_van.apt_hunter()

if __name__ == '__main__':
	main()