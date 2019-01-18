#not my original code, henry gets credit
#imports 
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time
from variables import *
import html2text
#website info and timer
count = 0
url = 'website'
interval = int(input('interval [seconds]: '))
if(interval <= 10):
    print('too low, defaulting to 15')
    interval = 15

	#twilio info
def send_message():
    client = Client(id, token)
    client.messages.create(body='you`re cute',to=yourphone,from_==twilio)

	#actual scrape
def scrape_site():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = str(soup)
    web_text = html2text.html2text(text)
    return(web_text)

#extra check?
while True:
    text_original = scrape_site()
    time.sleep(interval)
    text_updated = scrape_site()
    count += 1
    print('check ' + str(count))
    if(text_original != text_updated):
        print('changed')
        send_message()
        continue
