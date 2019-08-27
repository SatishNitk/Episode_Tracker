from django.db import models


class Show(models.Model):
    show_id = models.CharField(max_length=25)
    show_name = models.CharField(max_length=50)
    overview = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=25)
    status_watched = models.BooleanField(default=False)
    running_status=models.BooleanField(default=False)
    first_air = models.DateField()
    siteRating = models.DecimalField(max_digits=5, null=True, decimal_places=3, blank=True, default=0)
    userRating = models.DecimalField(max_digits=5, null=True, decimal_places=3, blank=True, default=0)
    network = models.CharField(max_length=50)
    genre_list = models.TextField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    Banner = models.CharField(max_length=100)
    air_time = models.CharField(max_length=20)

    def __str__(self):
        return self.show_name

    


class Season(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    number = models.IntegerField()
    status_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episodeName = models.CharField(max_length=50, blank=True, null=True)
    number = models.IntegerField()
    firstAired = models.DateField(null=True, blank=True)
    date_watched = models.DateField(null=True, blank=True, auto_now=True, auto_now_add=False)
    tvdbID = models.CharField(max_length=50)
    overview = models.TextField(null=True, blank=True)
    status_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.episodeName

