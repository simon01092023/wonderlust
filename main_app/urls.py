from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('postcards/', views.postcards_index, name='index'),
    path('postcards/<int:postcard_id>/', views.postcards_detail, name='detail'),
    path('postcards/create/', views.PostCardCreate.as_view(),
         name='postcards_create'),
    path('postcards/<int:pk>/update/',
         views.PostCardUpdate.as_view(), name='postcards_update'),
    path('postcards/<int:pk>/delete/',
         views.PostCardDelete.as_view(), name='postcards_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
