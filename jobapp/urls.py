from django.urls import path
from . import views

#connect homepage to index/about functions
urlpatterns = [
    path('', views.index, name='index' ),
    path('about/', views.about, name='about' )
]