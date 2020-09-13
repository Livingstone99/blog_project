from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to= 'images/')
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:200]
    def date_display(self):
        return self.pub_date.strftime('%b %e %Y')

class Comment(models.Model):
    name = models.CharField(max_length= 30,default='Anonymous', blank=True)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete= models.CASCADE, related_name='comments')

