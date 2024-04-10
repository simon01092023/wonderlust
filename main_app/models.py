from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Location(models.Model):
    name = models.CharField(max_length=100)
    # latitude = models.FloatField(max_length=90)
    # longitude = models.FloatField(max_length=180)
    latitude = models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)])
    def __str__(self):
        return self.name




class PostCard(models.Model):
    title = models.CharField(max_length=100,)
    date = models.DateField(("PostDate"), auto_now=False, auto_now_add=False)   
    content = models.TextField(max_length=250)
    locations = models.ManyToManyField(Location)

    # 1 user has many PostCards
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"postcard_id": self.id})
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    PostCard = models.ForeignKey(PostCard, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Photo for PostCard_id: {self.PostCard_id} @{self.url}"



