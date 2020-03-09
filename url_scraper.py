### LIBRARIES USED FOR THIS PROJECT ###
from bs4 import BeautifulSoup
import requests
import datetime
#import html_scraper

### SEND REQUEST TO GET WEBPAGE WE WANT TO PARSE ###
def getPage(url,headers):
    get_url = requests.get(url, headers = headers)
    web_cont = get_url.content
    return web_cont

url = 'https://www.bestbuy.com/site/desktop-computers/all-desktops/pcmcat143400050013.c?id=pcmcat143400050013&qp=customerreviews_facet%3DCustomer%20Rating~Top-Rated'

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36"
    }

web_page = getPage(url,headers)

### TURN WEBPAGE INTO OBJECT THAT CAN BE PARSED ###
def webParser(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup
parsed_page = webParser(web_page)


### PRINT PAGE CONTENTS TO TXT FILE ####
# string_page = str(parsed_page)
# with open('actual_page','a') as ap:
#     ap.write(string_page)

#### GRAB PRODUCT INFORMATION ###
products = parsed_page.find_all('li',{'class': 'sku-item'})

with open('products.csv','w') as pr:
    headers = 'item_id, item_name, item_rating, item_link, item_price\n'
    pr.write(headers)

    for product in products:
        item_name = product.img['alt']
        find_id = product.find_all('span', {'class': 'sku-value'})
        item_id = find_id[1].text
        item_rating = product.i['alt']
        item_link = product.a['href']
        find_price = product.find_all('span',{'aria-hidden':'true'})
        item_price = find_price[1].text
        #print(item_price.replace(',',''))

        pr.write(item_id + ',' + item_name + ',' + item_rating + ',' + item_link + ',' + item_price.replace(',','') + '\n')


    # print('item_name: ' + item_name)
    # print('item_id: ' + item_id)
    # print('item_rating ' + item_rating)
    # print('item_link ' + item_link)
    # print('item_price ' + item_price)



### GET INFO ON OBJECT AND PLACE IN EMPTY .TXT FILE ###

# tweet_urls = []
# a_tags = parsed_page.find_all('a')
# for element in a_tags:
#     urls = element.get('href')
#     tweet_urls.append(urls)
#
# with open('tweet_urls.txt','a') as tweet:
#     now = datetime.datetime.now()
#     tweet.write('%s\n'%now)
#     for listitem in tweet_urls:
#         tweet.write('%s\n' % listitem)
