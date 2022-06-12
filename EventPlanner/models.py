from django.db import models

# Create your models here.
class Event(models.Model):
	ssno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	description = models.TextField( max_length=90)
	thumbnail = models.ImageField(upload_to='static/images')
	slug = models.SlugField()
	date = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.title

	