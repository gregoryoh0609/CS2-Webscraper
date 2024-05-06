import requests
from bs4 import BeautifulSoup
import json
import csv
from discordwebhook import Discord
from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class WebDriver(object):
    def __init__(self):
        self.options = Options()
        
        self.options.add_argument('--headless')
    def get(self):
        driver = Firefox(options=self.options)
        return driver

def hover_action(driver,x,y,location):
    time.sleep(2)
    unhide_element = driver.find_element(By.ID,location)
    hover_action = ActionChains(driver)
    hover_action.move_to_element(unhide_element).perform()
    hover_action.move_by_offset(x,y).perform()
    time.sleep(3)
    print("Completed hover action")

def get_ban_info(driver):
    # ban_Info = driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div/div")
    # ban_Info = driver.find_element(By.XPATH,"//div[@class='highcharts-label highcharts-tooltip highcharts-color-undefined']")
    date = driver.find_element(By.XPATH,"/html/body/main/div/div[4]/div/div/span/div[1]")
    date = date.text.encode('ascii','ignore').decode('utf-8')
    day = int(date[:2])
    year = int(date[-2:])
    month = date.split(' ')[1]

    vac_num = driver.find_element(By.XPATH,"/html/body/main/div/div[4]/div/div/span/b[1]")
    vac_num = vac_num.text.encode('ascii','ignore').decode('utf-8')
    return {
        'Month' : month,
        'Day' : day,
        'Year' : year,
        'VAC_count' : vac_num
        }

# depreciated function         
# def decode_ban_info(data):
#     vac_Count = data.text.encode('ascii','ignore').decode('utf-8')
#     return vac_Count

