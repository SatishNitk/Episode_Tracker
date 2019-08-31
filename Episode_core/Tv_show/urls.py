"""Episode_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from Tv_show.views import HomePage_view, Add_show_view, home_view, SearchPage_view

urlpatterns = [
    path('home/', HomePage_view.as_view(), name="home"),
    path('homepage/', SearchPage_view.as_view(), name="homeview"),
    path('search/', SearchPage_view.as_view(), name="search"),
    path('show/', HomePage_view.as_view(), name="show"),
    path('add_show/', Add_show_view.as_view(), name="add_show"),
]
