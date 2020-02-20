# LIBRARIES USED FOR THIS PROJECT

from bs4 import BeautifulSoup
import requests
import datetime

# OPEN HTML AND PARSE IT
def htmlParser(html):
    with open(html, 'r+') as file:
        soup = BeautifulSoup(file, 'html.parser')
        return soup

html = input('Enter in a html file that you want to parse.')
parsed_doc = htmlParser('barrensavannah.html')
print(parsed_doc.prettify())

# GET INFO ON OBEJCT
# title = parsed_doc.title.name
# print(title)

a_tags = parsed_doc.find_all('a')
# print(a_tags)

# # p_tags = parsed_doc.find_all('p')
# print(p_tags)

# print(parsed_doc.title.string)
# print(parsed_doc.title.parent.name)
# print(parsed_doc.p)
# print(parsed_doc.p['class'])
# print(parsed_doc.find(id="footer"))
# print(parsed_doc.find(class_= 'contentBox'))


'''Change tag name'''
# tag = parsed_doc.p
# tag.name = 'h3'
# #print(type(tag))
# print(tag.name)
# print(parsed_doc.prettify())

# Extract all text from a page
#print(parsed_doc.get_text())

'''Extract all urls that contain 'clintonyates' '''

# linkage = parsed_doc.find_all('a')
# for link in linkage:
#     if 'clintonyates' in link.text:
#         print(link)
#         #print(link.attrs['href'])


# FIND ALL LINKS AND WRITE THEM TO A FILE
url_list = []

#
for element in a_tags:
    link = element.get('href')
    url_list.append(link)
    #print(url_list)

with open('savannah_urls.txt','a') as links:
    now = datetime.datetime.now()
    links.write('%s\n'%now)
    for listitem in url_list:
        links.write('%s\n'%listitem)
