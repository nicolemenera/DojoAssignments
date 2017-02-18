from django.conf.urls import url
from . import views

def to_run(request):
  print ("HELLO")
  print ("="*30)
  print ("HELP")
  
urlpatterns = [
    url(r'^$', views.index),
    url (r'^new_user$', views.new_user)
]