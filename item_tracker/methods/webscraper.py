import requests
from bs4 import BeautifulSoup


def scrapePage(shop, item_url):
    name = ''
    price = 0
    if shop == "Amazon":
        name, price, ori_price = getAmazonItemDetails(item_url)
    elif shop == "Newegg":
        name, price, ori_price = getNeweggItemDetails(item_url)
    elif shop == 'Book Depository':
        name, price, ori_price = getBookDepositoryItemDetails(item_url)
    price = round(price, 2)
    ori_price = round(ori_price, 2)
    return name, price, ori_price


def getNeweggItemDetails(item_url):
    page = requests.get(item_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find name of items
    name = soup.find("h1", {"class": "product-title"}).text

    # Find original price of item
    ori_price_block = soup.find("li", {"class": "price-was"})
    try:
        ori_price = ori_price_block.findChild("span").text
        ori_price = float(ori_price.replace("$", '').replace(",", ''))
        ori_price = usdToSgd(ori_price)
    except AttributeError:
        ori_price = None

    # Find current price of item
    price_block = soup.find("li", {"class": "price-current"})
    dollar = price_block.findChild("strong").text
    cent = price_block.findChild("sup").text
    price = dollar + cent
    price = float(price.replace(',', ''))
    price = usdToSgd(price)
    if ori_price is None:
        return name, price, price
    else:
        return name, price, ori_price


def getAmazonItemDetails(item_url):
    page = requests.get(item_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find name of items
    name = soup.find(id="productTitle").text
    # Amazon items are padded with \n, need to remove
    name = name.replace("\n", "")

    # Find price of item
    try:
        ori_price = soup.find("span", {"class": "priceBlockStrikePriceString"}).text
        ori_price = float(ori_price.replace("S$", '').replace(",", ''))
        price = soup.find(id="priceblock_dealprice").text
        price = float(price.replace("S$", '').replace(",", ''))
    except AttributeError:
        price = soup.find(id="priceblock_ourprice").text
        price = float(price.replace('S$', '').replace(',', ''))
        ori_price = None
    if ori_price is None:
        return name, price, price
    else:
        return name, price, ori_price


def getBookDepositoryItemDetails(item_url):
    page = requests.get(item_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find name of items
    name_block = soup.find("div", {"class": "item-info"})
    name = name_block.findChild("h1").text
    print(name)

    # Find price of item
    price = soup.find("span", {"class": "sale-price"}).text
    price = float(price.replace('$', '').replace(",", ''))
    print(price)
    # price = float(price.replace('S$', ''))
    return name, price


def usdToSgd(price):
    return price * 1.36
