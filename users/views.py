from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages

from .methods.registerMethods import createNewUser
from .methods.loginMethod import signInUser


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        isSuccessful = signInUser(request, username, password)
        if isSuccessful:
            messages.success(request, 'Account successfully created')  # Message is not showing
            return redirect('tracker-home')
        else:
            messages.info(request, "Account failed to create")  # Message is not showing
    return render(request, "users/login.html", {'title': 'Sign In'})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retypePassword = request.POST['retypePassword']
        isSuccessful = createNewUser(username, email, password, retypePassword)
        if isSuccessful:
            messages.success(request, 'Account successfully created')  # Message is not showing
            return redirect('login')
        else:
            messages.info(request, "Account failed to create")  # Message is not showing
    return render(request, "users/register.html", {'title': 'Sign Up'})
