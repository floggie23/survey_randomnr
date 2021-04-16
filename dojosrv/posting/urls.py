from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('view', views.index1), 
    path('back', views.back),
    path('number', views.number),
    path('generate', views.generate),
    path('reset', views.clear)
]
