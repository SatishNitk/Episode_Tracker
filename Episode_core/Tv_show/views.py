from django.shortcuts import render
from django.http import HttpResponse


def home_view(requests):
    return render(requests, "header.html")
