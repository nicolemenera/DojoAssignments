from django.shortcuts import render
from .models import models

def index(request):
  User.objects.create(first_name="Nikki", last_name="Menera", email="nikki@internet.com", password="something", created_at="", updated_at="")
  user = User.objects.all()
  print (user)
  return render(request, "the_wall/index.html")
# Create your views here.
