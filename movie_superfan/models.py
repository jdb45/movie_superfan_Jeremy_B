from django.db import models
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True

User._meta.get_field('email')._blank = False
User._meta.get_field('last_name')._blank = False
User._meta.get_field('first_name')._blank = False



class Movie(models.Model):

    title = models.CharField(max_length=200)
    backdrop = models.CharField(max_length=200, blank=True, null=True)
    movie_id = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    popularity = models.FloatField(blank=True, null=True)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.CharField(max_length=20)


    def __str__(self):
        return 'Movie title: {} ID: {} Backdrop: {} ' \
               'Description: {} Popularity: {} Poster_Path: {} Release_Date: {}'\
            .format(self.title, self.movie_id, self.backdrop,
                    self.description, self.popularity, self.poster_path, self.release_date)
