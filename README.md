# tutorial-django

## install up django (ubuntu 20.04)
```
pip3 install django

django-admin startproject project_name

python3 manage.py runserver

python manage.py startapp app_name
```

## initial steps

* Do the instilation
* Append the created app('hello') to project_name/project_name/settings.py under installed apps
* Code hello/views.py
* Create a urls.py file for hello to route the views
* Link the new unrl.py to the global urls.py