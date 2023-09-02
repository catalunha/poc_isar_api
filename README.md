
# History
(venv) catalunha@pop-os:~/apps/poc_isar_api$ python -m venv venv
(venv) catalunha@pop-os:~/apps/poc_isar_api$ source ./venv/bin/activate
create .gitignore e incluir venv 
se esquecer limpe o cache e reenvie.
(venv) catalunha@pop-os:~/apps/poc_isar_api$ git rm -r --cached .
(venv) catalunha@pop-os:~/apps/poc_isar_api$ pip install djangorestframework
(venv) catalunha@pop-os:~/apps/poc_isar_api$ pip freeze
asgiref==3.7.2
Django==4.2.4
djangorestframework==3.14.0
pytz==2023.3
sqlparse==0.4.4
typing_extensions==4.7.1

(venv) catalunha@pop-os:~/apps/poc_isar_api$ django-admin startproject project .
(venv) catalunha@pop-os:~/apps/poc_isar_api$ python manage.py migrate
(venv) catalunha@pop-os:~/apps/poc_isar_api$ python manage.py createsuperuser
Username (leave blank to use 'catalunha'): admin
Email address: 
Password: a
Password (again): a
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

(venv) catalunha@pop-os:~/apps/poc_isar_api$ python manage.py runserver

(venv) catalunha@pop-os:~/apps/poc_isar_api$ python -m venv venv
catalunha@pop-os:~/myapp/pocs/poc_isar_api$ source ./venv/bin/activate
(venv) catalunha@pop-os:~/myapp/pocs/poc_isar_api$ ls
db.sqlite3  pocisarapi  README.md         venv
manage.py   project     requirements.txt
(venv) catalunha@pop-os:~/myapp/pocs/poc_isar_api$ pip install -r requirements.txt 
Collecting