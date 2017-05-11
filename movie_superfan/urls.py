from django.conf.urls import url

from django.contrib.auth import views as auth_views
from . import views, views_movies, views_users



urlpatterns = [

    url(r'^$', views.homepage, name='homepage'),
    url(r'^logout/$', views_users.logout,name='logout_user'),

    url(r'^movies/$', views_movies.movie_list, name='movies'),
    url(r'^movies/detail/(?P<movie_pk>\d+)/$', views_movies.movie_detail, name='movie_detail'),
    url(r'^movies/search/$', views_movies.search_movies, name='movie_search'),

    url(r'^movies/add/watchlist/(?P<movie_pk>\d+)/$', views_movies.add_watchlist, name='add_watchlist'),
    url(r'^movies/add/viewed/(?P<movie_pk>\d+)/$', views_movies.add_viewed, name='add_viewed'),
    url(r'^movies/add/favorite/(?P<movie_pk>\d+)/$', views_movies.add_favorite, name='add_favorite'),

    url(r'^movies/profile/(?P<user_pk>\d+)/$', views_users.user_profile, name='user_profile'),
    url(r'^movies/profile/(?P<user_pk>\d+)/watchlist/$', views_users.user_watchlist, name='user_watchlist'),
    url(r'^movies/profile/(?P<user_pk>\d+)/viewedlist/$', views_users.user_viewlist, name='user_viewlist'),
    url(r'^movies/profile/(?P<user_pk>\d+)/favoritelist/$', views_users.user_favorite_list, name='user_favorite_list'),
]
