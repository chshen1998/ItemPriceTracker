from .webscraper import scrapePage
from .dbmanager import addItemToDB, updateItemInDB


def parseUrl(request, item_url):
    shop = getShopFromUrl(item_url)
    if shop:
        name, price, ori_price = scrapePage(shop, item_url)
        addItemToDB(name, shop, price, ori_price, item_url, request)


def refreshItemPrices(items):
    for item in items:
        name, price = scrapePage(item.shop, item.link)
        updateItemInDB(item, price)


def getShopFromUrl(item_url):
    try:
        # Get the host name from URL (e.g. www.amazon.sg)
        remove_https = item_url.split('//', 2)[1]
        hostname = remove_https.split('/', 2)[0]
    except IndexError:
        return False

    # Find the website name from host name
    if hostname == "www.amazon.sg":
        return "Amazon"
    elif hostname == "www.newegg.com":
        return "Newegg"
    elif hostname == "www.bookdepository.com":
        return "Book Depository"
    else:
        return None
