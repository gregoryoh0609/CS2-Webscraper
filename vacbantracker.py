import requests
from bs4 import BeautifulSoup
import json
import csv
from discordwebhook import Discord
from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

# Define your target URL
url = 'https://convars.com/csgostats/en/bans'
#https://stackoverflow.com/questions/39305877/can-i-scrape-the-raw-data-from-highcharts-js how to get raw data from highcharts.js
# raw data for vac bans and game bans are in tooltop. div class="highcharts-label highcharts-tooltip highcharts-color-undefined"
# use selenium to put mouse at the most recent day, then extract the data from the tooltip

options = webdriver.FirefoxOptions()
options.add_argument("-headless")
driver = webdriver.Firefox(options = options)
driver.get(url)
time.sleep(5)
htmlSource = driver.page_source
# Places cursor in middle of chart first to unhide hidden element that is responsible for the tooltip
unhide_element_event = driver.find_element(By.ID,"chart_bans180")
hover_action = ActionChains(driver)
hover_action.move_to_element(unhide_element_event).perform()
hover_action.move_by_offset(450,0).perform()

time.sleep(2)
ban_Info = driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div/div/span")

# encode data into ascii then decode that data into utf-8

vac_Count = ban_Info.text.encode('ascii','ignore').decode('utf-8')
print(vac_Count)


driver.quit()