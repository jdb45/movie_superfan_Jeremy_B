from django.shortcuts import render


def homepage(request):
    return render(request, 'movie_superfan/home.html')
