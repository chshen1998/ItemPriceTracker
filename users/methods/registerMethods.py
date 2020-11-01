from django.contrib.auth.models import User


def createNewUser(username, email, password, retypePassword):
    if isSamePassword(password, retypePassword):
        user = User.objects.create_user(username, email, password)
        user.save()
        return True
    else:
        return False


def isSamePassword(password, retypePassword):
    return password == retypePassword
