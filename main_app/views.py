from django.shortcuts import render, redirect
from .models import PostCard, Location
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
import googlemaps
from django.conf import settings
import os



class PostCardCreate(CreateView):
  model = PostCard
  fields = '__all__'

class PostCardUpdate(UpdateView):
  model = PostCard
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['title', 'date', 'content', 'locations']
  

class PostCardDelete(DeleteView):
  model = PostCard
  success_url = '/postcards'



def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def postcards_index(request):
    postcards = PostCard.objects.all()
  # We pass data to a template very much like we did in Express!
    return render(request, 'postcards/index.html', {
    'postcards': postcards
  })


def postcards_detail(request, postcard_id):
  postcard = PostCard.objects.get(id=postcard_id)
  return render(request, 'postcards/detail.html', { 'postcard': postcard })


def GeocodingHome(request):
    locations = Location.objects.all()
  # We pass data to a template very much like we did in Express!
    return render(request, 'locations/index.html', {
    'locations': locations
  })




class GeocodingView(View):
  template_name = 'WonderLust/geocoding.html'
  def get(self,request,pk):
    location = Location.objects.get(pk=pk)
    if location.address and location.country and location.zipcode and location.city !=None:
        address_string = str(location.address)+ "," +str(location.zipcode)+ "," + str(location.city)+ "," + str(location.country)
        #  link the google api key
        secret_key = os.environ['GOOGLE_API_KEY']
        gmap = googlemaps.Client(key= secret_key)
        # gmap = googlemaps.Client(key= settings.GOOGLE_API_KEY)
        result = gmaps.geocode(address_string)
    else:
        result = ''
    context = {
        'location':location,
        'result': result
    }
    return render(request, self.template_name, context)