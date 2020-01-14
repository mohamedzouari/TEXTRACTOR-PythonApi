from django.db import models
from django.db.models import Model 
# Create your models here. 
  
class ImageModel(Model): 
    image = models.ImageField(upload_to='images/') 
