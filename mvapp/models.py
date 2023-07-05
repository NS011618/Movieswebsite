from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from distutils.command.upload import upload
# Create your models here.
class mshow(models.Model):
    Moviename = models.CharField(max_length=150)
    Heroname = models.CharField(max_length=150)
    Heroiename = models.CharField(max_length=150)
    Director = models.CharField(max_length=150)
    Releasedate = models.DateField(default=None)    
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.URLField(max_length=1000)
    mimage=models.ImageField(null=True,blank=True,upload_to="images/")

def __str__(self):
    return self.name