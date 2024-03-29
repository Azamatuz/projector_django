from django.db import models

# Create your models here.
class Project(models.Model):
    province    = models.CharField(blank=True, max_length=10)
    institution = models.CharField(blank=True, max_length=100)
    leader      = models.CharField(blank=True, max_length=50)
    fund        = models.IntegerField(blank=True, null=True)
    date        = models.DateField(auto_now=False, auto_now_add=False)
    keywords    = models.CharField(blank=True, max_length=200)
    sector      = models.CharField(blank=True, max_length=50)
    discipline  = models.CharField(blank=True, max_length=100)
    year        = models.IntegerField(blank=True, null=True)
