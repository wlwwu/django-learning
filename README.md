# django-learning
django project via django rest framework

##create virutal environment and activate
python3.8 -m venv env

source env/bin/activate

##install required packages
pip install -r requirement.txt


##create a django project
django-admin.py startproject djangolearning .


##enable app for django
python manage.py startapp api


##create user database model


##set custom user model
under settings.py

##make migrations
python3 manage.py makemigrations api

python3 manage.py migrate

error: django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency api.0001_initial on database 'default'.

Delete the _pycache_ and the 0001_initial files.
Delete the db.sqlite3 from the root directory (be careful all your data will go away).

##create super user
python3 manage.py createsuperuser

##enable django admin

##APIView and ViewSet
1.APIView--need full control over your logic
         --processing files and rendering a synchoronous response
         --You are calling other APIs /services
         --Access local files or data


##serializer


