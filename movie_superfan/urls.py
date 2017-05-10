from django.conf.urls import url

from django.contrib.auth import views as auth_views
from . import views, views_movies, views_users



urlpatterns = [

    url(r'^$', views.homepage, name='homepage'),
    url(r'^movies/$', views_movies.movie_list, name='movies'),
    url(r'^movies/detail/(?P<movie_pk>\d+)/$', views_movies.movie_detail, name='movie_detail'),
    url(r'^movies/search/$', views_movies.search_movies, name='movie_search'),
    url(r'^movies/add/watchlist$', views_movies.add_watchlist, name='add_watchlist'),
    url(r'^movies/add/viewed$', views_movies.add_viewed, name='add_viewed'),
    url(r'^movies/profile/(?P<user_pk>\d+)/$', views_users.user_profile, name='user_profile'),
]
