# Better Home API
Online application for selling and buying houses


## how to run
1. install python3, pip3, virtualenv, MySQL in your system.
2. clone the project `git clone https://github.com/Sinaatkd/better-home-server.git`
3. in the `better_home_api/` folder, rename `.env.sample` to `.env`
4. db config are in `better_home_api/.env`
5. create a virtualenv named venv using `python -m virtualenv venv`
6. connect to virtualenv using `.\venv\Scripts\activate`
7. from the project folder, install packages using `pip install -r requirements.txt`
8. apply django models to database using `python manage.py migrate`
8. copy all files from your static folders into the STATIC_ROOT directory. using `python manage.py collectstatic`
9. now environment is ready. run it by `python manage.py runserver`

## generate secret key
1. run command `python manage.py shell`
2. enter following codes:
```
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```
3. and copy it

## create an admin user
1. run command `python manage.py create_superuser <username> <password> <phone_number>`
2. now you can move to /admin and login with created user
