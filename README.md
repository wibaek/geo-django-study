[GeoDjango Tutorial](https://docs.djangoproject.com/en/5.1/ref/contrib/gis/tutorial/)

```
pip freeze > requirements.txt

pip install -r requirements.txt
```

```
python3 manage.py runserver
```



### Create PostGIS Database
```sql
>>> createdb learn-geo-django-db
>>> psql learn-geo-django-db

CREATE EXTENSION postgis;
CREATE EXTENSION postgis_raster;.
CREATE USER geodjango PASSWORD 'my_passwd';
```

### Get sample data
```
wget https://web.archive.org/web/20231220150759/https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip
unzip TM_WORLD_BORDERS-0.3.zip
```

### Import sample data
```python
>>> python3 manage.py shell

from world import load
load.run()
```

### About GIS data
TM_WORLD_BORDERS-0.3.shp 파일을 DataSource로 읽어온다.

DataSource는 여러 Layer로 구성되어 있으나, shapefiles는 하나의 Layer만 가질 수 있다.

Layer는 geom_type을 가진다. 예시 데이터에서는 Polygon. Layer에는 다양한 reference system이 연관되어 있는데, 예를들어 layer.srs에 접근하면 SpatialReference 객체를 얻을 수 있다.

Layer은 여러 Feature로 구성되어 있는데, 이를 iterable 하게 접근할 수 있다.

Feature에서 feat.geom에 geometry 정보가 저장되어 있고, feat.geom.json으로 json 형태를 확인할 수 있다.

### Spatial Queries
```python
pnt_wkt = "POINT(-95.3385 29.7245)"
from world.models import WorldBorder
WorldBorder.objects.filter(mpoly__contains=pnt_wkt)
```
위와 같이 Point가 Polygon에 포함되는지 확인할 수 있다.

```python
from django.contrib.gis.geos import Point
pnt = Point(12.4604, 43.9420)
WorldBorder.objects.get(mpoly__intersects=pnt)
```
위와 같이 Point가 Polygon과 교차하는지(포함하거나 겹치는지) 확인할 수 있다.