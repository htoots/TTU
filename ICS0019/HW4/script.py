"""
Task

Create a Python spider for page:
https://ordi.eu/lauaarvutid?___store=en&___from_store=et (English)
or
https://ordi.eu/lauaarvutid (Estonian)
Grab all computers from all pages and create JSON file with attributes:
{Product name: '', Price: '', Picture href: ''}


By: Hannes Toots
"""

import requests
import json
from lxml import etree

def getRequest(url):
    """
    Function to get request from given url
    :param url: url to get request from
    :return: requests.get(url)
    """
    return requests.get(url)

def treeQuery(request):
    """
    Function to get the element tree from an html literal
    :param request: HTML request
    :return: etree.html(request.text)
    """
    return etree.HTML(request.text)

def getData(tree):
    """
    Function to get data from the query
    :param tree: tree from treeQuery()
    :return dataList: dictionary list with needed data
    """
    dataList = []

    # Get amount of href's to get the amount of computers
    # Nice div class name by the website
    count = tree.xpath('count(//div[@class="category-products "]//h2[@class="product-name"])')

    # Never used lxml, i dont know how to put count and products into
    # same line, if possible.
    products = tree.xpath('//div[@class="category-products "]')

    for i in range(int(count)):
        for product in products:
            href = product.xpath('.//h2/a/@href')[i]
            name = product.xpath('.//h2/a/@title')[i]
            price = product.xpath('.//div[@class="price-box"]/span/text()')[i]

            dataList.append({
                "Product name":'%s'%name,
                "Price":'%s'%price,
                "Href":'%s'%href
            })

    return dataList

def saveData(list, name="jsondata.txt"):
    """
    Function to save a JSON file with list dump
    :param list: dictionary list to dump into file
    :param name: name of file to save
    :return:
    """
    with open(name, 'w') as out:
        json.dump(list, out, sort_keys=True)

def main():
    site = "https://ordi.eu/lauaarvutid?___store=en&___from_store=et&limit=all"
    req = getRequest(site)
    tree = treeQuery(req)
    list = getData(tree)
    saveData(list)

if __name__ == '__main__':
    main()
