''' Libraries used for this project '''

from bs4 import BeautifulSoup
#import lxml
import requests

'''Get webpage we want to parse'''
result = requests.get('https://twitter.com/i/events/1228706829011566593')
src = result.content
#print(result.content)
#print(result.status_code)
#print(result.headers)

'''Turn webpage into an object and parse it. '''
soup = BeautifulSoup(src, 'html.parser')
#print(soup.prettify())

'''Get info on object'''

#links = soup.find_all('a')
#print(links)


# print(soup.a)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.find_all('a'))
# print(soup.find(id="footnote"))
# print(soup.find(class_= 'story'))

'''Change tag name'''
# tag = soup.p
# tag.name = 'h3'
# #print(type(tag))
# print(tag.name)
# print(soup.prettify())

''' Extract all urls from page 'a' tags'''

# for link in soup.find_all('a'):
#     links = link.get('href')
#     print(links)
#
# ''' Extract all text from a page '''
# print(soup.get_text())

'''Extract all urls that contain 'clintonyates' '''

# linkage = soup.find_all('a')
# for link in linkage:
#     if 'clintonyates' in link.text:
#         print(link)
#         #print(link.attrs['href'])
