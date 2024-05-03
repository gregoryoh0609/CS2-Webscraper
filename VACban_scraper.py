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

def hover_action(driver):
    time.sleep(2)
    unhide_element = driver.find_element(By.ID,"chart_bans180")
    hover_action = ActionChains(driver)
    hover_action.move_to_element(unhide_element).perform()
    hover_action.move_by_offset(450,0).perform()
    time.sleep(2)
    print("Completed hover action")

def get_ban_info(driver):
    ban_Info = driver.find_element(By.XPATH,"/html/body/main/div/div[4]/div/div")
    return ban_Info
        
def decode_ban_info(data):
    vac_Count = data.text.encode('ascii','ignore').decode('utf-8')
    return vac_Count


url = 'https://convars.com/csgostats/en/bans'

instance_ = WebDriver()
driver = instance_.get()
driver.get(url)
hover_action(driver)
ban_Info = get_ban_info(driver)
vac_Count = decode_ban_info(ban_Info)
print(vac_Count)
driver.quit


