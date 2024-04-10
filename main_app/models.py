from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(min_value=-90, max_value=90)
    longitude = models.FloatField(min_value=-180, max_value=180)




class PostCard(models.Model):
    title = models.CharField(max_length=100)
    date = models.models.DateField(_(""), auto_now=False, auto_now_add=False)   
    content = models.TextField(max_length=250)
    locations = models.ManyToManyField(Location)

    # 1 user has many PostCards
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"PostCard_id": self.id})
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    Journal = models.ForeignKey(PostCard, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Photo for PostCard_id: {self.PostCard_id} @{self.url}"



