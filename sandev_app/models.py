from django.db import models
from django_countries.fields import CountryField
# Create your models here.
category = (
    ('web','web'),
    ('app', 'app'),
)
class ProjectDetail(models.Model):
    project_name = models.CharField(max_length=50, blank=True)
    cover_image = models.FileField(max_length=50, blank=True)
    project_category = models.CharField(max_length=50, blank=True, choices=category,)
    project_client = models.CharField(max_length=50, blank=True)
    project_date = models.DateField(max_length=50, blank=True)
    project_url = models.CharField(max_length=50, blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField(blank=True)

class ClientFeedback(models.Model):
    name = models.CharField(max_length=50, blank=True)
    Country = CountryField(blank=True)
    image = models.FileField(blank=True)
    feedback = models.TextField(blank=True)