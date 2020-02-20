# Libraries used for this project
from bs4 import BeautifulSoup
import requests

# Get webpage we want to parse
get_url = requests.get('https://twitter.com/i/events/1228706829011566593')
web_cont = get_url.content

# Turn webpage into an object and parse it.
soup = BeautifulSoup(web_cont,'html.parser')

# Get info on object and place in empty .txt file
tweet_urls = []
a_tags = soup.find_all('a')
for element in a_tags:
    urls = element.get('href')
    tweet_urls.append(urls)

with open('tweet_urls.txt','a') as tweet:
    for listitem in tweet_urls:
        tweet.write('%s\n' % listitem)
