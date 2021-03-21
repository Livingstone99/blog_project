from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    tag = models.CharField(max_length=20)
    def __str__(self):
        return self.tag

class Blog(models.Model):

    title = models.CharField(max_length= 70)
    post_category = models.ManyToManyField(Category, default = 'solar')
    summary = models.TextField(max_length=100, default='Good read')
    pub_date = models.DateTimeField()

    # paragraph1 = models.TextField(max_length=500, blank=True)
    # first_image = models.ImageField(upload_to='1st_image', blank=True)
    #
    # paragraph2 = models.TextField(max_length=500, blank=True)
    # first_image1 = models.ImageField(upload_to='2nd_image', blank=True)
    #
    # paragraph3 = models.TextField(max_length=500, blank=True)
    # first_image2 = models.ImageField(upload_to='3rd_image', blank=True)
    #
    body = RichTextField(max_length=1500, blank=True, help_text='share link of images that are light')
    image = models.ImageField(upload_to= 'images/', help_text='drastically reduce the quality of the image to nothing more than 100kb')
    alternative_text = models.CharField(max_length=15, default='dreamfix', help_text='cation the image')
    home_display = models.BooleanField(default=False, help_text='when this is ticked, the image appears at the home page article index')
    def __str__(self):
        return self.title
    # def summary(self):
    #     return self.body[:200]
    def date_display(self):
        return self.pub_date.strftime('%b %e %Y')

class Comment(models.Model):
    name = models.CharField(max_length= 30,default='Anonymous', blank=True)
    body = models.TextField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete= models.CASCADE, related_name='comments')

