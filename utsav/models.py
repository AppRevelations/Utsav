from django.db import models

# Create your models here.
class Fest(models.Model):
    fest_name = models.CharField(max_length=256)
    fest_desc = models.CharField(max_length=1000)
    place = models.CharField(max_length=128)
    timings = models.CharField(max_length=100)
    image_url = models.URLField()

    #def __unicode__(self):
        #return self.fest_name
	
class Event(models.Model):
    fest_id= models.CharField(max_length=256)
    event_name = models.CharField(max_length=256)
    event_desc = models.CharField(max_length=1000)
    place = models.CharField(max_length=128)
    timings = models.CharField(max_length=100)
    image_url = models.URLField()
    contact_person= models.CharField(max_length=256)
    contact_number= models.CharField(max_length=20)
	
class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    email_id = models.EmailField()
    contact_number = models.CharField(max_length=20)
    image_url = models.URLField()
