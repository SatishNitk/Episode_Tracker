from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from Tv_show.utils.util import *
from Tv_show.models import Show, Season, Episode
from django.contrib.auth.models import User
from django.contrib import auth


def home_view(requests):
    return render(requests, 'Tv_show/homepage.html')


class HomePage_view(View):
    def get(self, requests):
        all_show = Show.objects.all()
        context = {
         'shows': all_show,
        }
        return render(requests, 'Tv_show/home.html', context)

    def post(self, requests):
        all_show = Show.objects.all()
        context = {
            'shows': all_show,
        }
        return render(requests, 'Tv_show/home.html', context)


class Add_show_view(View):
    """ """
    def post(self, requests):
        print("user data..", requests.user)
        tvdbID = requests.POST.get('show_id')
        running_status = requests.POST.get('runningStatus')
        slug = ''
        try:
            show = Show.objects.get(tvdbID=tvdbID, user=requests.user)
            slug = show.slug
        except Show.DoesNotExist as e:
            show_data = get_series_with_id(tvdbID)
            show = Show()
            show.add_show(show_data, running_status, requests.user)
            slug = show.slug
            all_season = get_all_episodes(tvdbID, 1)
            for i in range(len(all_season)):
                string = 'Season' + str(i+1)
                season_data = all_season[string] # episode in a single season
                season = Season()
                season.add_season(show, i+1)
                for season_episode in season_data:
                    if season_episode['episodeName']:
                        episode = Episode()
                        episode.add_episode(season, season_episode)

        return HttpResponse("all saved")


class SearchPage_view(View):
    """ """
    def post(self, requests):
        show_name = requests.POST.get('search_string')
        if show_name == "":
            return render(requests, "Tv_show/homepage.html")
        else:
            show_datalist = search_series_list(show_name)
            context = {}
            context['show_detail'] = True
            context['show_datalist'] = show_datalist[0]
            return render(requests, "Tv_show/homepage.html", {'context': context})

    def get(self, requests):
        """ """
        context = {}
        context['show_detail'] = False
        return render(requests, "Tv_show/homepage.html", {'context': context})


class AllShow_view(View):
    """ """
    def get(self, requests):
        pass

class LoginLogout_view(View):
    """ """
    pass


class Signup_view(View):
    """ """
    def post(self, requests):
        """ """

        if requests.POST['password1'] == requests.POST['password2']:
            try:
                User.objects.get(username=requests.POST['username'])
                return HttpResponse("user already exists")
            except User.DoesNotExist:
                user = User.objects.create_user(username=requests.POST['username'], password=requests.POST['password1'])
                auth.login(requests, user)
                return HttpResponse("done succ")
        return render(requests, "header.html", {'error':'failed'})


class Logout_view(View):
    """ """
    def get(self, requests):
        auth.logout(requests)
        return redirect('homeview')


class Login_view(View):
    """ """
    def post(self, requests):
        # print("shsghjgsjgs ",requests.POST.get('password',"sjagsjgsghsggshgsa "))
        user = auth.authenticate(username = requests.POST['username1'], password= requests.POST['password'])
        if user is not None:
            auth.login(requests, user)
            return redirect('homeview')
        else:
            return HttpResponse("faild to login")


class Allshow_view(View):
    """ """
    def get(self, requests):
        all_show = Show.objects.filter(user=requests.user)
        return render(requests, 'Tv_show/all_show.html',{'all_show':all_show})
