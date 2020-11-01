import math
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from .methods.dbmanager import deleteItemFromDB
from .methods.parser import parseUrl, refreshItemPrices
from .models import Item


@csrf_exempt
@login_required()
def home(request):
    if request.method == "POST":
        if 'track_button' in request.POST:
            item_url = request.POST['item_url']
            parseUrl(request, item_url)
        elif 'delete_button' in request.POST:
            item_id = request.POST['delete_button'].split(" ", 2)[1]
            deleteItemFromDB(item_id)
        elif 'refresh_button' in request.POST:
            itemsToRefresh = Item.objects.filter(user=request.user)
            refreshItemPrices(itemsToRefresh)
        elif 'logout_button' in request.POST:
            logout(request)
            messages.success(request, "Successfully signed out")  # Not showing
            return redirect('login')
    items = Item.objects.filter(user=request.user)
    #  num_rows = int(math.ceil(len(items)/3.0))
    return render(request, 'item_tracker/home.html', {'items': items})


def recommendations(request):
    return render(request, 'item_tracker/recommendations.html', )



