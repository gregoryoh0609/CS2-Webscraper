import requests
from bs4 import BeautifulSoup
import json
import csv
from discordwebhook import Discord
from io import StringIO
from html.parser import HTMLParser
from VACban_scraper import WebDriver, hover_action, get_ban_info
def get_json(text):
    json_data = json.loads(str(text))
    return json_data

def get_recent_data(json):
    vac_Count = 0 
    notes = json['events'][0]['announcement_body']['body']
    notes = notes[16:-9]
    date = json['events'][0]['event_name']
    notes_split = notes.split(' ')
    for word in notes_split:
        if word.lower() == "vac":
            vac_Count +=1
    return {
        'Date' : date,
        'Notes' : notes,
        'VACcount' : vac_Count
    }

def get_html(link):
    response = requests.get(link)
    html = response.text
    return html

# curr_date = []
# file_name = 'recentupdate.csv'
# # Defining target URL
# patch_url = 'https://store.steampowered.com/events/ajaxgetpartnereventspageable/?clan_accountid=0&appid=730&offset=0&count=100&l=english&origin=https://www.counter-strike.net'
# discord_url = "https://discord.com/api/webhooks/1235077710385250366/XuJNVGPZg9gl9wNh7JYxouEbj2-IXa4MYU-d_oSWyDvCHL-wguEKy9tJazjBtvL6Phho"

# # Fetch the HTML content
# html_content = get_html(patch_url)
# # Parse the HTML content using Beautiful Soup
# soup = BeautifulSoup(html_content, 'html.parser')
# json_data = get_json(soup.text)
# recent_Notes = get_recent_data(json_data)
# print(recent_Notes)

vac_url = 'https://convars.com/csgostats/en/bans'

instance_ = WebDriver()
driver = instance_.get()
driver.get(vac_url)
hover_action(driver,450,0,"chart_bans180")
ban_Info = get_ban_info(driver)

print(ban_Info)
driver.quit


















# TODO: Count how many times VAC is mentioned and show the count on the title 
# TODO: Create logic to display image or gif if the word VAC is mentioned or not in the patch notes
# TODO: Use AWS Lambda, Amazon S3 and Amazon Event bridge to automate the scraping

# with open(file_name, "r",newline = '', encoding="utf-8") as f:
#     csvreader=csv.reader(f)
#     prev_date = list(csvreader)
# prev_date_conversion = ''.join(prev_date[0])

# embed = {
#     "title": curr_date[-1],
#     "description": patch_Notes
# }
# message = {
#     "embeds":[embed]
# }

# # Just checking if they are differnet patchnotes, will be holding the date of prev patchnotes in csv file   
# if curr_date[-1] != prev_date_conversion:
#     with open(file_name,"w",newline='', encoding = "utf-8") as f:
#         csvwriter = csv.writer(f)
#         csvwriter.writerow(curr_date)
#         response = requests.post(discord_url,json = message)

# Print formatted JSON content
