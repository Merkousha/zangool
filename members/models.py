from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True,blank=True,)#upload_to=get_file_path
    
