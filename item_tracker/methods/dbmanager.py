from item_tracker.models import Item


def addItemToDB(name, shop, price, ori_price, link, request):
    # item = Item(name, shop, price, link)
    item = Item(name=name, shop=shop, current_price=price, lowest_price=price, original_price=ori_price, link=link)
    item.user = request.user
    item.save()


def deleteItemFromDB(item_id):
    Item.objects.filter(id=item_id).delete()


def updateItemInDB(item, price):
    if price < item.lowest_price:
        item.lowest_price = price
    item.current_price = price
    item.save(update_fields=['current_price', 'lowest_price'])
