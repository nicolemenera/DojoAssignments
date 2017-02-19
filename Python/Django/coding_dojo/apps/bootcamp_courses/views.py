from django.shortcuts import render, redirect, HttpResponse
from .models import Course
import re

def index(request):
  print "*****************"
  context = {'courses': Course.objects.all()}
  return render(request, "bootcamp_courses/index.html", context)
  
def process(request):
  print "*****************"
  if request.method == "GET":
    return redirect('/')
  check = Course.objects.filter(name = request.POST['name'])
  if len(check) > 0:
    redirect('/')
  Course.objects.create(name=request.POST['name'], description=request.POST['description'])
  return redirect ('/')
  
def delete(request, id):
  context = {'courses': Course.objects.filter(id=id)}
  return render(request, 'courses/delete.html', context)
  
def actual_delete(request, id):
  Course.objects.filter(id=id).delete()
  return redirect('/')
# Create your views here.
