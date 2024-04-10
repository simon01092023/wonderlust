from django.shortcuts import render, redirect
from .models import PostCard

from django.views.generic.edit import CreateView, UpdateView, DeleteView



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
