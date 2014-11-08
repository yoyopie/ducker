from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
import web_site.models
from django.contrib.auth.decorators import login_required
import forms


# Create your views here.
def login(request):
    userform = forms.UserForm()
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/index/')
    context = {
        'userform': userform,
    }
    return render_to_response("login.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")
