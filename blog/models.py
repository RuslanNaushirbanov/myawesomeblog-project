from django.db import models

# Create your models here.

class Blog(models.Model):
	blog_title = models.CharField(max_length=50)
	blog_date = models.DateField(auto_now_add=True)
	blog_text = models.TextField()
	blog_image = models.ImageField(upload_to='blog_images/')