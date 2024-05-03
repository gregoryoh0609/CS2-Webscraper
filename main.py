import requests
from bs4 import BeautifulSoup
import json
import csv
from discordwebhook import Discord
curr_date = []
file_name = 'recentupdate.csv'
# Defining target URL
url = 'https://store.steampowered.com/events/ajaxgetpartnereventspageable/?clan_accountid=0&appid=730&offset=0&count=100&l=english&origin=https://www.counter-strike.net'

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
# TODO: Use AWS Lambda, Amazon S3 and Amazon Event bridge to automate the scraping

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
