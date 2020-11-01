from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .options import tit
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pictiure = models.ImageField(null=True,blank=True)
    title = models.CharField(choices=tit,null=True, max_length=10)
    description= models.TextField(null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    cat_pic = models.ImageField(upload_to='upload')
    cat_name = models.CharField(max_length=23, verbose_name='Category Name')
    

    def __str__(self):
        return self.cat_name


class Property(models.Model):
    prop_pic = models.ImageField(
        upload_to='upload/', verbose_name='Property Picture')
    STATUS = (
        ('RENT', 'RENT'),
        ('FOR SALE', 'FOR SALE'),
    )
    street_name = models.CharField(max_length=234)
    city = models.CharField(max_length=234)
    price = models.FloatField(max_length=234)
    bedroom = models.PositiveIntegerField()
    garage = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)
    property_status = models.CharField(max_length=24, choices=STATUS)
    garage = models.PositiveIntegerField()
    prop_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cat = models.ManyToManyField(Category, verbose_name='Property Category')
    property_size = models.PositiveIntegerField()

    def __str__(self):
        return self.street_name
    
    


class Agents(models.Model):
    agent_picture = models.ImageField(upload_to='upload/')
    agent_name = models.CharField(max_length=25,)
    email = models.EmailField(blank=True, null=True)
    agent_phone = models.CharField(max_length=11, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.agent_name


class Service(models.Model):
    service_title = models.CharField(max_length=80)
    service_content = models.CharField(max_length=234, unique=True)

    def __str__(self):
        return self.service_title


class Blog(models.Model):
    blog_pic = models.ImageField(
        upload_to='upload/', verbose_name='Blog Picture')
    blog_title = models.CharField(max_length=344, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog_content = models.TextField(max_length=500000, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title


class Dapo(models.Model):
    pass
