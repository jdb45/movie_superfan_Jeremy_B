# Movie Super Fan

This is a web app that allows users to keep track of movies they like.


## Some of the features:
# *Displays my cool logo ;)
<img width="1275" alt="screen shot 2017-05-11 at 12 50 00 am" src="https://cloud.githubusercontent.com/assets/22032532/25934560/40df1d92-35e4-11e7-85c7-b51108fe4e3a.png">

# *Displaying the user profile
<img width="1275" alt="screen shot 2017-05-11 at 12 51 59 am" src="https://cloud.githubusercontent.com/assets/22032532/25934562/469bd04a-35e4-11e7-9efc-9e9dcb61effc.png">
<img width="1280" alt="screen shot 2017-05-11 at 12 52 07 am" src="https://cloud.githubusercontent.com/assets/22032532/25934601/7d8bd79e-35e4-11e7-9cff-1690481a604d.png">
<img width="1280" alt="screen shot 2017-05-11 at 12 51 42 am" src="https://cloud.githubusercontent.com/assets/22032532/25934604/7d965bc4-35e4-11e7-8727-6b75e4f17fb9.png">
<img width="1277" alt="screen shot 2017-05-11 at 12 51 51 am" src="https://cloud.githubusercontent.com/assets/22032532/25934605/7d9a170a-35e4-11e7-8a3b-70920ddbd9db.png">



# *Searching the movies
<img width="1274" alt="screen shot 2017-05-11 at 12 51 09 am" src="https://cloud.githubusercontent.com/assets/22032532/25934600/7d86d898-35e4-11e7-8734-cf2b3fa7730d.png">


# *The selected movie
<img width="1277" alt="screen shot 2017-05-11 at 12 51 21 am" src="https://cloud.githubusercontent.com/assets/22032532/25934602/7d8eb90a-35e4-11e7-8392-df1d6665c0f6.png">


It is recommended to use Google Chrome and to disable network the cache. 

This is done be doing these steps:

`click the settings icon on top right corner| More Tools | Developer Tools | Network | Disable cache`
### Running the app
The app starts with no data. Searching for movies sends API requists to The Movie Database and returns the results. There for 

### This product uses the TMDb API but is not endorsed or certified by TMDb. You must follow their rules when using their API!

The celebs tab does not work yet.

### Install postgresql

https://github.com/DjangoGirls/tutorial-extensions/blob/master/optional_postgresql_installation/README.md

Set the admin password.

Start postgres running

`su postgres ` if on a mac/linux

`pg_ctl start`  enter username and password

start postgres shell with `psql`

And create a user called lmnop

```
create user superfan with password 'password_here'; 
```

create a database superfan  (Or whatever you want to call it)

```
create database superfan owner superfan;
```

### Environment variable 

set environment variable called
`POSTGRES_SUPERFAN_USER_PASSWORD`
set the value to superfan's user password

(PC users, follow directions here. http://www.computerhope.com/issues/ch000549.htm. Mac & Linux users follow this https://natelandau.com/my-mac-osx-bash_profile/

(Mac users may need to run these commands; these one time; replace 9.6 with your version of PostGreSQL, if it's different

`sudo ln -s /Library/PosgreSQL/9.6/lib/libssl.1.0.0.dylib /usr/local/lib
sudo ln -s /Library/PosgreSQL/9.6/lib/libcrypto.1.0.0.dylib /usr/local/lib`

And this when you start a new shell; or set it permanently in .bash_profile, again replace 9.6 with your version if different.
`export DYLD_FALLBACK_LIBRARY_PATH=/Library/PostgreSQL/9.6/lib:$DYLD_LIBRARY_PATH`
)

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
`THE_MOVIE_DB_KEY`

