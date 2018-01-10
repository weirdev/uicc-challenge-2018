from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print(request.user)
    template = loader.get_template("mail/index.html")
    context = {}
    return HttpResponse(template.render(context, request))
