from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('postcards/', views.postcards_index, name='index'),
    path('postcards/<int:postcard_id>/', views.postcards_detail, name='detail'),
    path('postcards/create/', views.PostCardCreate.as_view(), name='postcards_create'),
    path('postcards/<int:pk>/update/', views.PostCardUpdate.as_view(), name='postcards_update'),
    path('postcards/<int:pk>/delete/', views.PostCardDelete.as_view(), name='postcards_delete'),
    path('locations/', views.postcards_index, name='index'),
    path('postcards/<int:postcard_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),
    path('postcards/<int:postcard_id>/add_photo/', views.add_photo, name='add_photo'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/', views.LocationList.as_view(), name='location_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
    path('accounts/signup/', views.signup, name='signup')]
