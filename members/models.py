from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time']

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
