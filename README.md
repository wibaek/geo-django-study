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
CREATE EXTENSION postgis_raster;.
CREATE USER geodjango PASSWORD 'my_passwd';
```

### Get sample data
```
wget https://web.archive.org/web/20231220150759/https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip
unzip TM_WORLD_BORDERS-0.3.zip
```