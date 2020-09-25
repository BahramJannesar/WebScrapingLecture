from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import os


chromedriver = "/home/mars/Desktop/WebScrapingCoruse/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_option = Options()
chrome_option.add_argument("--start-maximized")
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_option)
actions = ActionChains(driver)

def save_object( file_name  , saved_object , writing_method):

    saved_object = json.dumps(saved_object, indent=3 , ensure_ascii=False)
    with open(file_name, writing_method) as handler:
        handler.writelines(saved_object + ',')


def main():

    timeout =  30
    i = 0
    all_links = []

    with open('car_links.json' , 'r') as file:
        car_links = json.load(file)
    
    while i <= 4 :
        for link in car_links[i]['links']:
            all_links.append(link)
        i += 1
    
    for car in all_links:

        car_data = {}
        driver.get(car)
        try :
            show_phone_number_button = driver.find_element_by_css_selector('#phone-open')
            show_phone_number_button.click()

            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "addetail-single-phone-number", " " ))]')))
            phone_number = driver.find_element_by_css_selector('.addetail-single-phone-number').text

            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//p[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]')))

            car_data = {

                'announcement_time ' : driver.find_element_by_xpath('//p[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]').text , 
                'kilometer' : driver.find_element_by_xpath('//p[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]').text ,
                'gear_box_type' : driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "inforight", " " ))]//p[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]').text ,
                'fuel_type' : driver.find_element_by_xpath('//p[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]').text ,
                'body' : driver.find_element_by_xpath('//p[(((count(preceding-sibling::*) + 1) = 7) and parent::*)]').text , 
                'color' : driver.find_element_by_xpath('//p[(((count(preceding-sibling::*) + 1) = 8) and parent::*)]').text , 
                'state' : driver.find_element_by_xpath('//p[(((count(preceding-sibling::*) + 1) = 9) and parent::*)]').text ,
                'city' : driver.find_element_by_xpath('//p[(((count(preceding-sibling::*) + 1) = 10) and parent::*)]').text ,
                'phone_number' : phone_number
            }
        
            save_object('data.json' , car_data , 'a')
        except:
            
            car_data = {

                'announcement_time ' : None , 
                'kilometer' : None ,
                'gear_box_type' : None ,
                'fuel_type' : None ,
                'body' : None, 
                'color' : None , 
                'state' : None ,
                'city' : None ,
                'phone_number' : None
            }

            save_object('data.json' , car_data , 'a')



if __name__ == "__main__":

    main()