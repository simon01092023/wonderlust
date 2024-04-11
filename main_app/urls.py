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
    
    path('geocoding/<int:pk>/', views.GeocodingView.as_view(), name='my_geocoding_view'),
    path('geocodingHome/', GeocodingHome.as_view(), name='my_home_view'),
    path('locations/', views.postcards_index, name='index'),
 

]
