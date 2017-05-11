# Movie Super Fan

This is a web app that allows users to keep track of moives they like.


### To install

1. Create and activate a virtual environment. Use Python3 as the interpreter.

2. pip install -r requirements.txt

3. cd movie_superfan/superfan

4. python manage.py makemigrations

5. python manage.py migrate

6. python manage.py runserver

Site at

127.0.0.1:8000

### Create superuser

from movie_superfan/superfan

python manage.py createsuperuser

enter username and password

You will be able to use these to log into admin console at

127.0.0.1:8000/admin


### The Movie Database keys
For this program to work you need API keys from TMDb.

Create a TMDb account
[Get API keys from TMDb](https://www.themoviedb.org/). The following keys must
be stored as system environment variables:
* THE_MOVIE_DB_KEY

