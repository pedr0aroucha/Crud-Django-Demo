from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('read', views.read),
    path('update', views.update), #search
    path('update/<user>', views.delete),
    path('delete', views.delete), #search
    path('delete/<user>', views.delete),
]
