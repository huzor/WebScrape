''' Libraries used for this project '''

from bs4 import BeautifulSoup
#from python-lxml import html
import requests

'''Open html doc & parse it '''
with open('scrape_doc.html') as am:
    soup = BeautifulSoup(am, 'html.parser')
#print(soup.prettify())

'''Navigate the data structure'''
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

tag = soup.p
print(type(tag))
