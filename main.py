# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# URL = 'https://www.counter-strike.net/news/updates'
# # page= requests.get(URL)
# # soup = BeautifulSoup(page.text, 'html.parser')
# # results = soup.find(id="application_config")
# # print(results)
 
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
 
# driver.get(URL) 
# wait = WebDriverWait(driver, 10)
# print(driver.page_source.encode("utf-8"))
# driver.quit()

import requests
from bs4 import BeautifulSoup
import json
import csv
from discordwebhook import Discord
curr_date = []
file_name = 'recentupdate.csv'
# Define your target URL
url = 'https://store.steampowered.com/events/ajaxgetpartnereventspageable/?clan_accountid=0&appid=730&offset=0&count=100&l=english&origin=https://www.counter-strike.net'
# discord = Discord(url="https://discord.com/api/webhooks/1235077710385250366/XuJNVGPZg9gl9wNh7JYxouEbj2-IXa4MYU-d_oSWyDvCHL-wguEKy9tJazjBtvL6Phho") 
# Send an HTTP GET request and fetch the HTML content
response = requests.get(url)
discord_url = "https://discord.com/api/webhooks/1235077710385250366/XuJNVGPZg9gl9wNh7JYxouEbj2-IXa4MYU-d_oSWyDvCHL-wguEKy9tJazjBtvL6Phho"
# Fetch the HTML content
html_content = response.text
    
# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

json_data = json.loads(str(soup.text))


curr_date.append(json_data['events'][0]['announcement_body']['headline'])
patch_Notes = json_data['events'][0]['announcement_body']['body']
patch_Notes = patch_Notes[16:-9]

# TODO: Count how many times VAC is mentioned and show the count on the title 
# TODO: Create logic to display image or gif if the word VAC is mentioned or not in the patch notes


with open(file_name, "r",newline = '', encoding="utf-8") as f:
    csvreader=csv.reader(f)
    prev_date = list(csvreader)
prev_date_conversion = ''.join(prev_date[0])

embed = {
    "title": curr_date[-1],
    "description": patch_Notes
}
message = {
    "embeds":[embed]
}

# Just checking if they are differnet patchnotes, will be holding the date of prev patchnotes in csv file   
if curr_date[-1] != prev_date_conversion:
    with open(file_name,"w",newline='', encoding = "utf-8") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(curr_date)
        response = requests.post(discord_url,json = message)






    


    

# Print formatted JSON content
