from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length = 100,null=True)
    password = models.CharField(max_length=8,null=True)
    
    
    def __str__(self):
        return self.name
    
    
    
    
    