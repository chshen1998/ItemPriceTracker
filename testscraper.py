import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.sg/Soundance-Aluminum-Computer-Ergonomic-Compatible/dp/B07NXR9R22?ref_=Oct_s9_apbd_orec_hd_bw_b78ROd9&pf_rd_r=1XZ4JE5447GB325X2XHB&pf_rd_p=02b5afe1-8a27-52fb-9897-3d552f6ff188&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=6537670051"
def usdToSgd(price):
    return price * 1.36

def getAmazonItemDetails(item_url):
    page = requests.get(item_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find name of items
    name = soup.find(id="productTitle").text
    # Amazon items are padded with \n, need to remove
    name = name.replace("\n", "")

    try:
        ori_price = soup.find("span", {"class": "priceBlockStrikePriceString"}).text
        #ori_price = ori_price.findChild("span").text
        ori_price = float(ori_price.replace("S$", '').replace(",", ''))
        price = soup.find(id="priceblock_dealprice").text
        price = float(price.replace("S$", '').replace(",", ''))
    except AttributeError:
        # Find price of item
        price = soup.find(id="priceblock_ourprice").text
        price = float(price.replace('S$', '').replace(',', ''))
        ori_price = None

    if ori_price is None:
        return name, price, price
    else:
        return name, price, ori_price

name, price, ori_price = getAmazonItemDetails(URL)
print(price)
print(ori_price)
