from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to= 'images/')
    title = models.CharField(max_length=100, default= 'solar installation')
    summary  = models.CharField(max_length = 200
                                )
    def __str__(self):
        return self.title

class FeedBack(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.name
