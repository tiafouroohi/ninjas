from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index),
    path("process",views.process),
    path("other", views.other)
]