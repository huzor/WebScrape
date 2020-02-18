from bs4 import BeautifulSoup
import requests

get_url = requests.get('https://twitter.com/i/events/1228706829011566593')
web_cont = get_url.content
soup = BeautifulSoup(web_cont,'html.parser')

tweet_urls = []
a_tags = soup.find_all('a')
for element in a_tags:
    urls = element.get('href')
    tweet_urls.append(urls)

with open('tweet_urls.txt','a') as tweet:
    for listitem in tweet_urls:
        tweet.write('%s\n' % listitem)
