# LIBRARIES USED FOR THIS PROJECT

from bs4 import BeautifulSoup
import requests
import datetime

# OPEN HTML AND PARSE IT
def soupParser(html):
    with open(html, 'r+') as file:
        soup = BeautifulSoup(file, 'html.parser')
        return soup

html = input('Enter in a html file that you want to parse.')
parsed_doc = soupParser('barrensavannah.html')
print(parsed_doc.prettify())

# with open('barrensavannah.html', 'r+') as file:
#     soup = BeautifulSoup(file, 'html.parser')
#     # print(soup.prettify())

# GET INFO ON OBEJCT
# title = soup.title.name
# print(title)

a_tags = soup.find_all('a')
# print(a_tags)

# # p_tags = soup.find_all('p')
# print(p_tags)

# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.find(id="footer"))
# print(soup.find(class_= 'contentBox'))


'''Change tag name'''
# tag = soup.p
# tag.name = 'h3'
# #print(type(tag))
# print(tag.name)
# print(soup.prettify())

# Extract all text from a page
#print(soup.get_text())

'''Extract all urls that contain 'clintonyates' '''

# linkage = soup.find_all('a')
# for link in linkage:
#     if 'clintonyates' in link.text:
#         print(link)
#         #print(link.attrs['href'])


# FIND ALL LINKS AND WRITE THEM TO A FILE
url_list = []

#
# for element in a_tags:
#     link = element.get('href')
#     url_list.append(link)
#     print(url_list)
#
# with open('savannah_urls.txt','a') as links:
#     now = datetime.datetime.now()
#     links.write('%s\n'%now)
#     for listitem in url_list:
#         links.write('%s\n'%listitem)
