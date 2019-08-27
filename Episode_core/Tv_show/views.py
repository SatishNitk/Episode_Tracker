from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from Tv_show.utils.util import *
from Tv_show.models import *

def home_view(requests):
    return render(requests, 'Tv_show/home.html')

class HomePage_view(View):
    def get(self, requests):
        all_show = Show.objects.all()
        context = {
        'shows':all_show,
        }
        return render(requests, 'Tv_show/home.html', context)

    def post(self, requests):
        all_show = Show.objects.all()
        context = {
        'shows':all_show,
        }
        return render(requests, 'Tv_show/home.html', context)
