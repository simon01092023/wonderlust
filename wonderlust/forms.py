# from django.forms import ModelForm
# from .models import PostCard, Location

# class PostCardForm(ModelForm):
# 	class Meta:
# 		# meta class is configuration options for a class
# 		# this is straight from the docs
# 		model = PostCard
# 		fields = ['date', 'meal']


from django import forms
from .models import Map


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['address', 'geolocation']

