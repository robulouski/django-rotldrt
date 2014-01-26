from __future__ import unicode_literals 
from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required


def home(request):
    if (request.user.is_authenticated()):
        return render(request, 'demo/home.html')
    return login(request, template_name='demo/home.html')

@login_required
def profile(request):
    return login(request, template_name='demo/profile.html')
