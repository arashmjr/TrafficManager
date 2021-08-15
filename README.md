# TrafficManager
A traffic management software that allows us to store cars, drivers, roads, and tolls in the system
And it provides the ability to record car tolls. Also, road cameras record the cars that are moving, which allows us to identify the location of a car when we want.
And reports such as the Amount of toll and make it possible to list vehicles based on defined variables

## How to run
To run TrafficManager in development mode; Just use steps below:
1. Install python3.8.0, pip, virtualenv in your system.
2. Clone the project https://github.com/arashmjr/TrafficManager.
3. Make development environment ready using commands below.

```bash
git clone https://github.com/arashmjr/TrafficManager && cd TrafficManager
virtualenv venv   # Create virtualenv named venv
venv\Scripts\activate # If You're On A Windows Machine
source venv/bin/activate # If You're On A Linux
pip install -r requirements.txt
install and configuration of postgresql using the following sections 
python manage.py makemigration and python manage.py make migrate  # Create database tables
```
4. Run TrafficManager using python manage.py runserver

## django_postgresql
using postgresql database with django
## INSTALLATION
Install the postgresql database in your local computer first from the .exe file on the official site.

Install the postgresql package for python - psycopg2 using pip in virtualenv
## CONFIGURE

Create a new database using the postgresql command line.

CREATE DATABASE TrafficManager

Inside our django project settings.py, set the database as the postgresql like so,
```bash
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'TrafficManager',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',

    }
```
Just create models and run python manage.py makemigrations and migrate command, the new database should work fine.

## Note 
If you think this repo need to have new usecase feel free to add an issue or send a pull request.

## Author
arashmjr, arash.mjr@gmail.com

