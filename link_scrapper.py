import json
import requests
from bs4 import BeautifulSoup
import time


def save_object( file_name  , saved_object , writing_method):

    saved_object = json.dumps(saved_object, indent=3 , ensure_ascii=False)
    with open(file_name, writing_method) as handler:
        handler.writelines(saved_object + ',')


def car_links_scrapper():

    page_number = 1

    while page_number <= 5:

        save_dict = {}
        car_links_list = []

        response = requests.get('https://bama.ir/car/bmw/all-models/all-trims?page={}'.format(page_number))

        soup = BeautifulSoup(response.content , 'html.parser' )

        cars_divider = soup.find('div' , attrs={'class':'eventlist car-ad-list-new clearfix'})

        car_links = cars_divider.find_all('div' ,  attrs={'class':'listdata'})

        for each in car_links:
            final_links = each.find('a' , attrs = { 'class': 'cartitle cartitle-desktop'})
            car_links_list.append(final_links.get('href'))

        save_dict = {
                'page_number': page_number,
                'links':car_links_list
            }

        save_object('car_links.json' , save_dict , 'a')

        page_number += 1

def car_data_scrapper():

    with open('car_links.json' , 'r') as file:
        car_links = json.load(file)
    
    i = 0
    all_links = []
    while i <= 4 :
        for link in car_links[i]['links']:
            all_links.append(link)
        i += 1

        for car in all_links:
            try:
                car_data = {}
                response = requests.get(car)
                soup = BeautifulSoup(response.text , 'html.parser')
                car_data = {

                    'car_name': soup.find('h1' , attrs = { 'class': 'addetail-title'}).text.strip(),
                    'motor_vol': soup.find('li' , attrs = { 'class': 'ad-detail-spec-11'}).text.strip(),
                    'car_silandrs': soup.find('li' , attrs = { 'class': 'ad-detail-spec-10'}).text.strip(),
                    'car_acceleration': soup.find('li' , attrs = { 'class': 'ad-detail-spec-14'}).text.strip(),
                    'car_consumption': soup.find('li' , attrs = { 'class': 'ad-detail-spec-16'}).text.strip()
                }
                save_object('car_data.json' , car_data , 'a')
            except:
                car_data = {

                    'car_name': soup.find('h1' , attrs = { 'class': 'addetail-title'}).text.strip(),
                    'motor_vol': None,
                    'car_silandrs': None,
                    'car_acceleration': None,
                    'car_consumption': None
                }
                save_object('car_data.json' , car_data , 'a')

                continue

if __name__ == "__main__":

    start = time.time()
    #car_links_scrapper()
    car_data_scrapper()
    print(time.time() - start)
    