from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import os


DOMAIN_URL = os.environ("DOMAIN_URL")

response = requests.get(DOMAIN_URL)

URL_HTML = response.text

soup = BeautifulSoup(URL_HTML, 'html.parser')

# pprint(URL_HTML)

property_addresses = soup.find_all(name='a', class_='address is-two-lines css-1y2bib4')
property_prices = soup.find_all(name='p', class_='css-mgq8yx')
address_list = []
links = []
link_list = []
price_list = []


# Addresses
for address in property_addresses:
    address_list.append(address.text)
# Links
for address in property_addresses:
    link_list.append(address.get('href'))
# Price per week
for address in property_prices:
    price_list.append(address.text.split()[0])

# pprint(link_list)
# pprint(address_list)
# pprint(price_list)


FORM_URL = os.environ("FORM_URL")
driver = webdriver.Chrome(executable_path=os.environ("CHROME_DRIVER_PATH"))
driver.get(FORM_URL)


for n in range(len(link_list)):
    driver.get(FORM_URL)

    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(address_list[n])
    price.send_keys(price_list[n])
    link.send_keys(link_list[n])
    submit_button.click()