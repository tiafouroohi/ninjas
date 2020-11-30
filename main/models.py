from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
