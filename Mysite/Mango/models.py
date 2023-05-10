from django.db import models

# Create your models here.
class BGRemover(models.Model):
    #name = models.CharField(max_length=50, blank=True, null=True)
    Image = models.ImageField(upload_to='images/',blank=True, null=True)