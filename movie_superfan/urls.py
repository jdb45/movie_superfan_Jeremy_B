from django.conf.urls import url

from django.contrib.auth import views as auth_views
from . import views, views_movies



urlpatterns = [

    url(r'^$', views.homepage, name='homepage'),
    url(r'^movies/$', views_movies.movie_list, name='movies'),
    url(r'^movies/detail/(?P<movie_pk>\d+)/$', views_movies.movie_detail, name='movie_detail'),

]
