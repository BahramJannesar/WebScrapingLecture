from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import json
import os



chromedriver = "/home/mars/Desktop/WebScrapingCoruse/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
actions = ActionChains(driver)

def save_object( file_name  , saved_object , writing_method):

    saved_object = json.dumps(saved_object, indent=3 , ensure_ascii=False)
    with open(file_name, writing_method) as handler:
        handler.writelines(saved_object )


def main():

    timeout =  30

    driver.get('https://bama.ir/car/detail-g97qyd9r-bmw-x4-28-2017')


    element = driver.find_element_by_xpath('//*[(@id = "phone-open")]')
    element.location_once_scrolled_into_view

    show_phone_number_button = driver.find_element_by_css_selector('#phone-open')
    show_phone_number_button.click()

    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "addetail-single-phone-number", " " ))]')))

    phone_number = driver.find_element_by_css_selector('.addetail-single-phone-number').text

    print(phone_number)




if __name__ == "__main__":

    main()