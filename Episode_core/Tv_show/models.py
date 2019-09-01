from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.text import slugify


class Show(models.Model):
    tvdbID = models.CharField(max_length=25)
    showName = models.CharField(max_length=50)
    overview = models.CharField(max_length=100)
    imdbID = models.CharField(max_length=25)
    statusWatched = models.BooleanField(default=False)
    runningStatus = models.CharField(max_length=50)
    firstAired = models.DateField(null=True, blank=True)
    siteRating = models.DecimalField(max_digits=5, null=True, decimal_places=3, blank=True, default=0)
    userRating = models.DecimalField(max_digits=5, null=True, decimal_places=3, blank=True, default=0)
    network = models.CharField(max_length=50)
    genreList = models.TextField(null=True, blank=True)
    lastUpdated = models.DateTimeField(null=True, blank=True)
    banner = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.showName

    def add_show(self, show_data, running_status):
        """ """
        self.tvdbID = show_data['tvdbID']
        self.showName = show_data['seriesName']
        self.overview = show_data['overview']
        self.imdbID = show_data['imdbID']
        self.runningStatus = running_status
        self.siteRating = show_data['siteRating']
        self.network = show_data['network']
        self.genreList = show_data['genre']
        self.lastUpdated = timezone.now()
        self.banner = 'http://thetvdb.com/banners/' + show_data['banner']
        self.slug = slugify(self.showName)
        print(show_data)
        try:
            print(show_data['firstAired'])
            if show_data['firstAired']:
                print("comig---")
                self.firstAired = datetime.strptime(str(show_data['firstAired']), '%Y-%m-%d').date()
            else:
                print("cmfffff fjfnfknk")
        except Exception:
            pass
        self.save()


class Season(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    number = models.IntegerField()
    statusWatched = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number)

    def add_season(self, show, season_number):
        self.show = show
        self.number = season_number
        self.save()


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episodeName = models.CharField(max_length=50, blank=True, null=True)
    episodeNumber = models.IntegerField()
    firstAired = models.DateField(null=True, blank=True)
    dateWatched = models.DateField(null=True, blank=True, auto_now=True, auto_now_add=False)
    tvdbID = models.CharField(max_length=50)
    overview = models.TextField(null=True, blank=True)
    statusWatched = models.BooleanField(default=False)

    def __str__(self):
        return self.episodeName

    def add_episode(self, season, season_data):
        """ """
        self.season = season
        self.episodeName = season_data['episodeName']
        self.episodeNumber = season_data['number']
        self.firstAired = season_data['firstAired']
        self.tvdbID = season_data['tvdbID']
        self.overview = season_data['overview']

        self.save()
