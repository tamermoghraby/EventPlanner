from asyncio.windows_events import NULL
from time import timezone
from unittest.util import _MAX_LENGTH
import django
from django.db import models

# Create your models here.
class Blog(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	content = models.TextField()
	short_des = models.CharField(max_length=300, default="")
	slug = models.CharField(max_length=100)
	time = models.DateTimeField(default=django.utils.timezone.now)

	def __str__(self):
		return self.title
    
	
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    desc = models.TextField(max_length=300, default="")
    time = models.DateTimeField(default=django.utils.timezone.now)
	
	

	
