from django.conf.urls import url
from . import views

# def index(request):
#   print ("YAAASSSS")

# Models -- views -- CONTROLLER
urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate$', views.generate),
]