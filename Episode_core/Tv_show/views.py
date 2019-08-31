from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from Tv_show.utils.util import *
from Tv_show.models import Show, Season, Episode


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
        tvdbID = requests.POST.get('show_id')
        running_status = requests.POST.get('runningStatus')
        slug = ''
        try:
            show = Show.objects.get(tvdbID=tvdbID)
            slug = show.slug
        except Show.DoesNotExist as e:
            show_data = get_series_with_id(tvdbID)
            show = Show()
            show.add_show(show_data, running_status)
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
            return render(requests, "Tv_show/homepage.html", {'context':context})
    def get(self, requests):
        """ """
        context = {}
        context['show_detail'] = False
        return render(requests, "Tv_show/homepage.html", {'context':context})

