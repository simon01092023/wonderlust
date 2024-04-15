
import uuid
import boto3
import os
from django.shortcuts import render, redirect
from .models import PostCard, Location, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Login
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Authorization 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
	error_message = ''
	if request.method == "POST":
		# create the user form object 
		# request.POST is the contents of the form
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# save the user to the database
			user = form.save() # this adds user to the table in psql
			# login our user
			login(request, user)
			return redirect('index') # index is the name of the url path
		else:
			error_message = "Invalid signup - try again"
	form = UserCreationForm()
	return render(request, 'registration/signup.html', {
		'error_message': error_message,
		'form': form
	})


def add_photo(request, postcard_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
          
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
           
            Photo.objects.create(url=url, postcard_id=postcard_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', postcard_id=postcard_id)

def disassoc_location(request, postcard_id, location_id):
	postcard = PostCard.objects.get(id=postcard_id)
	postcard.locations.remove(location_id)
	return redirect('detail',postcard_id=postcard_id)

# cats/<int:cat_id>/assoc_toy/<int:toy_id>/
def assoc_location(request, postcard_id, location_id):
	print(postcard_id, location_id )
	postcard = PostCard.objects.get(id=postcard_id)
	PostCard.locations.add(location_id)# adding a row to our through table the one with 2 foriegn keys in sql
	return redirect('detail', postcard_id=postcard_id)

class PostCardCreate(LoginRequiredMixin, CreateView):
  model = PostCard
  fields = ['title', 'date', 'content']

class PostCardUpdate(LoginRequiredMixin, UpdateView):
  model = PostCard
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['title', 'date', 'content']
  

class PostCardDelete(LoginRequiredMixin, DeleteView):
  model = PostCard
  success_url = '/postcards'


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    locations = Location.objects.all()
    
    return render(request, 'home.html',{
        'locations': list(locations.values())
    })


def about(request):
    return render(request, 'about.html')

def postcards_index(request):
    postcards = PostCard.objects.all()
  # We pass data to a template very much like we did in Express!
    return render(request, 'postcards/index.html', {
    'postcards': postcards
  })

@login_required 
# decorator function, the function called before detail page 
def postcards_detail(request, postcard_id):
  postcard = PostCard.objects.get(id=postcard_id)
  ##get the location postcaerd do not have
  id_list = postcard.locations.all().values_list('id')
  ##using exclude to query id not in list
  locations_postcard_doesnt_have = Location.objects.exclude(id__in=id_list)


  return render(request, 'postcards/detail.html', { 
       'postcard': postcard,
        'locations': locations_postcard_doesnt_have })


def assoc_location(request, postcard_id, location_id):
  PostCard.objects.get(id=postcard_id).locations.add(location_id)
  return redirect('detail', postcard_id=postcard_id)


class LocationList(ListView):
    model = Location

class LocationDetail(DetailView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'

