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


chromedriver = "/home/mars/Desktop/WebScrapingCoruse/scrapingWithSelenium/chromedriver"
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

    print('Hi Guys!!!')






if __name__ == "__main__":
    main()