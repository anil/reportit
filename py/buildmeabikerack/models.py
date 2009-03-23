from django.contrib.gis.db import models

# Create your models here.


class Rack(models.Model): 
    date = models.DateTimeField()    
    location = models.CharField(max_length=200)
    location_meta = models.CharField(max_length=200)
    meta = models.TextField()
    contact_email = models.EmailField()
    STATUS_STATE  = ( 
        ('st', 'start'),
        ('as', 'asses'),
        ('fn','finished'),
    )
    status = models.CharField(max_length=2, choices=STATUS_STATE)


class Neighborhoods(models.Model):
    gid = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=43)
    city = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    regionid = models.DecimalField(max_digits=65535, decimal_places=65535)
    the_geom = models.MultiPolygonField() 
    objects = models.GeoManager()

    class Meta:
        db_table = u'buildmeabikerack_neighborhoods'

