from mailservice import send_mail
from cl_housing import Housing

def main():
    # send_mail('test')
    apt_van = Housing(city='vancouver', category='apa', filters={'max_price': 1800, 'min_bedrooms': 2, 'search_distance': 5.5, 'zip_code':'V5Z+1M9'})
    print(apt_van.get_apartments())

if __name__ == '__main__':
	main()