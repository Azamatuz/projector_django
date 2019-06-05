from django.db import models

# Create your models here.
class Leader(models.Model):
    name = models.CharField(blank=True, max_length=50)
class Institution(models.Model):
    name = models.CharField(blank=True, max_length=100)
class Project(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    leader      = models.ManyToManyField(Leader)
    fund        = models.IntegerField(blank=True, null=True)
    date        = models.DateField(auto_now=False, auto_now_add=False)
    keywords    = models.CharField(blank=True, max_length=200)
    sector      = models.CharField(blank=True, max_length=50)
    discipline  = models.CharField(blank=True, max_length=100)
    year        = models.IntegerField(blank=True, null=True)
class Province(models.Model):
    name    = models.CharField(blank=True, max_length=10)
    projects = models.ManyToManyField(Project)