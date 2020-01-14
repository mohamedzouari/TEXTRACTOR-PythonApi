from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('convert/', views.convert, name='convert'),
    
]

#endpoint for the conversion service :http://localhost:8000/textractor/convert/