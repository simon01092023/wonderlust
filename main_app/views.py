from django.shortcuts import render, redirect
from .models import PostCard

from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class PostCardCreate(LoginRequiredMixin, CreateView):
  model = PostCard
  fields = '__all__'

class PostCardUpdate(LoginRequiredMixin, UpdateView):
  model = PostCard
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['title', 'date', 'content', 'locations']
  

class PostCardDelete(LoginRequiredMixin, DeleteView):
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

@login_required 
# decorator function, the function called before detail page 
def postcards_detail(request, postcard_id):
  postcard = PostCard.objects.get(id=postcard_id)
  return render(request, 'postcards/detail.html', { 'postcard': postcard })
