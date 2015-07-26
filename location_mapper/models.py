from django.db import models
import datetime
# Create your models here.
class VehicleLocation(models.Model):
    device_id= models.CharField(max_length=10)
    lat=models.FloatField()
    lon=models.FloatField()
    time= models.DateTimeField(default=datetime.datetime.now)
    def __unicode__(self):
        return self.device_id
