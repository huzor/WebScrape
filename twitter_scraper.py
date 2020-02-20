# Libraries used for this project
from bs4 import BeautifulSoup
import requests
import datetime
#import html_scraper

# Get webpage we want to parse
def getPage(url):
    get_url = requests.get(url)
    web_cont = get_url.content
    # print(web_cont)
    # print(get_url.status_code)
    # print(get_url.headers)
    return web_cont
url = input('Enter in a URL that you want parsed')
web_page = getPage(url)

# Turn webpage into an object that can be parsed.
def webParser(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup

parsed_page = webParser(web_page)

# Get info on object and place in empty .txt file
tweet_urls = []
a_tags = parsed_page.find_all('a')
for element in a_tags:
    urls = element.get('href')
    tweet_urls.append(urls)

with open('tweet_urls.txt','a') as tweet:
    now = datetime.datetime.now()
    tweet.write('%s\n'%now)
    for listitem in tweet_urls:
        tweet.write('%s\n' % listitem)
