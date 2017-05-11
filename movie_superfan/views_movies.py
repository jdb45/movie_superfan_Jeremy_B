from .forms import NewMovieForm, NewListForm
import os
from .models import Movie, Lists
from django.shortcuts import render, redirect, reverse, get_object_or_404
import tmdbsimple as tmdb
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash

tmdb.API_KEY = os.environ['THE_MOVIE_DB_KEY']

def movie_list(request):

    movies = Movie.objects.all().order_by('title')

    return render(request, 'movie_superfan/movies/movie.html',
                  {'movies': movies})

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movie_superfan/movies/movie_detail.html', {'movie': movie})


def search_movies(request):

    if request.method == 'POST':
        post_request = request.POST
        user_search = str(post_request['search']) # getting the user search
        search = tmdb.Search()
        response = search.movie(query=user_search)
        for s in search.results:
            form = NewMovieForm()
            if Movie.objects.filter(movie_id=str(s['id'])).exists():
                pass
            if str(s['adult']) == 'true':
                pass
            else:
                note = form.save(commit=False)
                note.title = s['title']
                note.backdrop = 'https://image.tmdb.org/t/p/w500' + str(s['backdrop_path'])
                note.movie_id = s['id']
                note.description = s['overview']
                note.popularity = s['popularity']
                note.poster_path = 'https://image.tmdb.org/t/p/w500' + str(s['poster_path'])
                note.release_date = s['release_date']
                note.save()



    return redirect('movies')


@login_required
def add_watchlist(request, movie_pk):

    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':

        form = NewListForm(request.POST)

        new_list = form.save(commit=False)

        new_list.user = request.user
        new_list.movie = movie
        new_list.watch_list = True
        new_list.save()
        return redirect('movies')


    return redirect('movies')

@login_required
def add_viewed(request, movie_pk):

    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':

        form = NewListForm(request.POST)

        new_list = form.save(commit=False)

        new_list.user = request.user
        new_list.movie = movie
        new_list.viewed = True
        new_list.save()
        return redirect('movies')

    return redirect('movies')


@login_required
def add_favorite(request, movie_pk):

    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':

        form = NewListForm(request.POST)

        new_list = form.save(commit=False)

        new_list.user = request.user
        new_list.movie = movie
        new_list.favorite = True
        new_list.save()
        return redirect('movies')

    return redirect('movies')
