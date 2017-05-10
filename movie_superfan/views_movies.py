from .models import Movie
from django.shortcuts import render, redirect, reverse, get_object_or_404



def movie_list(request):

    movies = Movie.objects.all().order_by('title')

    return render(request, 'movie_superfan/movies/movie.html',
                  {'movies': movies})

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movie_superfan/movies/movie_detail.html', {'movie': movie})
