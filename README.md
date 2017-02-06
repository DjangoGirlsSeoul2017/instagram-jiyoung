# Create Pystagram with Django
Reference : http://blog.hannal.com/category/start-with-django-webframework/

1. Create virtual environment and activate
```
$ python -m venv
$ python -m venv myvenv
$ source myvenv/bin/activate
```
2. Install django and start project
```
$ pip install django
$ django-admin startproject pystagram
```
3. Create superuser to better manage admin site and run server
```
$ python manage.py createsuperuser
$ python manage.py runserver
```
4. Start app and install pillow for ImageField
```
$ python manage.py startapp photos
$ pip install pillow
```
5. Make migrations and migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```
