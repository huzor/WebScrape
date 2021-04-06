### LIBRARIES USED FOR THIS PROJECT ###
from bs4 import BeautifulSoup
import requests


### SEND REQUEST TO GET BEST BUY WEBPAGE WE WANT TO PARSE ###
def getPage(url,headers):
    get_url = requests.get(url, headers = headers)
    web_cont = get_url.content
    return web_cont

url = 'https://www.bestbuy.com/site/desktop-computers/all-desktops/pcmcat143400050013.c?id=pcmcat143400050013&qp=customerreviews_facet%3DCustomer%20Rating~Top-Rated'

headers = {
    "User-Agent":"{Add browser info here}"
    }
web_page = getPage(url,headers)

### PRINT PAGE CONTENTS TO TXT FILE (used to verify that you have your intended page) ####
# string_page = str(parsed_page)
# with open('actual_page','a') as ap:
#     ap.write(string_page)

### TURN WEBPAGE INTO OBJECT THAT CAN BE PARSED ###
def webParser(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup
parsed_page = webParser(web_page)

#### GRAB PRODUCT INFORMATION AND PLACE IT INTO CSV ###
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

        pr.write(item_id + ',' + item_name + ',' + item_rating + ',' + item_link + ',' + item_price.replace(',','') + '\n')
