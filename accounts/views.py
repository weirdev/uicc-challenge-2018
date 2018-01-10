from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth import logout as dj_logout
from django.contrib.auth import login as dj_login
from django.views.generic import View


class LoginView(View):
    def get(self, request):
        template = loader.get_template("accounts/login.html")
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        user = authenticate(request, username=request.POST['username'], 
            password=request.POST['password'])
        if user is not None:
            dj_login(request, user)
        else:
            print("cats")
        return HttpResponseRedirect(request.POST.get('next', '/'))

def logout(request):
    dj_logout(request)
    return HttpResponseRedirect('/login')