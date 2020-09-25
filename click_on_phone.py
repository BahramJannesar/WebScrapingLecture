from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import os

chromedriver = "home/mars/Desktop/WebScrapingCoruse/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
actions = ActionChains(driver)

driver.get('https://bama.ir/car/detail-g97qyd9r-bmw-x4-28-2017')


show_phone_number_button = driver.find_element_by_xpath('//*[(@id = "phone-open")]')
show_phone_number_button.click()