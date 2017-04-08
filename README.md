################################################
# [Project]: Django - Pick Me (Web Application)
[Reference]:
1) https://blog.liang2.tw/posts/2015/10/django-draw-member/#data-in-orm-and-fixtures
2) https://github.com/ccwang002/draw_member_django
################################################

## Open a directory 
root@HelloWorld:~# mkdir DjangoTest
## Change directory to /DjangoTest
root@HelloWorld:~# cd ./DjangoTest
## Install virtual environment 
root@HelloWorld:~/DjangoTest# pip install virtualenv
## Enable a virtual environment 
root@HelloWorld:~/DjangoTest# virtualenv VENV
## Start virtual environment
root@HelloWorld:~/DjangoTest# source ./VENV/bin/activate
## Install django, unicodecsv lib
(VENV) root@HelloWorld:~/DjangoTest# pip install django unicodecsv
## Open django project
(VENV) root@HelloWorld:~/DjangoTest# django-admin startproject pickme

## Hierarchy is like below
```
DjangoTest/
└── pickme/
   ├── pickme/
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   └── manage.py
```
## Change directory to /pickme
(VENV) root@HelloWorld:~/DjangoTest# cd ./pickme
## Test Django server
(VENV) root@HelloWorld:~/DjangoTest/pickme# python manage.py runserver 8001

## ======== Checkpoint here =========
http://127.0.0.1:8001

## Open the first Django app
(VENV) root@HelloWorld:~/DjangoTest/pickme# python manage.py startapp polls

## Hierarchy is like below
```
DjangoTest/
└── pickme/
   ├── pickme/
   │   ├── ...
   ├── polls/
   │   ├── admin.py
   │   ├── apps.py
   │   ├── __init__.py
   │   ├── migrations/
   │   ├── models.py
   │   ├── tests.py
   │   └── views.py
   ├── manage.py
   └── db.sqlite3
```

## :+1: Patch to your django project!!
