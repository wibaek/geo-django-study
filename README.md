[GeoDjango Tutorial](https://docs.djangoproject.com/en/5.1/ref/contrib/gis/tutorial/)

```
pip freeze > requirements.txt

pip install -r requirements.txt
```

```
python3 manage.py runserver
```



### Create PostGIS Database
```
createdb learn-geo-django-db
psql learn-geo-django-db

CREATE EXTENSION postgis;
CREATE USER geodjango PASSWORD 'my_passwd';
```
