from django.db import models

class AuthorInfo(models.Model):
    full_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    phrase = models.CharField(max_length=100)
    desc = models.TextField()
    
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    
    img_1 = models.ImageField(upload_to='images/home/')
    img_2 = models.ImageField(upload_to='images/home/')

    logo = models.ImageField(upload_to='images/home/', default='logo')
    
    def __str__(self):
        return self.full_name
