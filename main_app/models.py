from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django_google_maps import fields as map_fields


class Location(models.Model):
    name = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)
    # latitude = models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)])
    # longitude = models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)])

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("locations_detail", kwargs={"pk": self.id})


class Map(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.address


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
    postcard = models.ForeignKey(PostCard, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for postcard_id: {self.postcard_id} @{self.url}"
