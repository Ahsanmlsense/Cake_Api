from distutils.archive_util import make_zipfile
from unicodedata import category
from django.db import models
from django.forms import CharField
import uuid

# Create your models here.

class Cakes(models.Model):
    """"Model of the cake having attributes name, flavour , cake_category , description
                all the attributes are complusory but id is assigned automatically no need 
                to assign id """
    name = models.CharField(max_length=32,blank=False,null=False)
    flavour = models.CharField(max_length=32,blank=False,null=False)
    cake_category = models.CharField(max_length=32)
    description = models.TextField(max_length=200)
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False,
         auto_created=True)
    
    def __str__(self) -> str:
        return self.name + " " + self.flavour
    