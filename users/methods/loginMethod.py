from django.contrib.auth import authenticate, login


def signInUser(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    else:
        return False
