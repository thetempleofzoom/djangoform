from django.urls import path
from . import views

#connect homepage to index function
urlpatterns = [
    path('', views.index, name='index' )
]