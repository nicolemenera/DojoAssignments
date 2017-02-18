from django.shortcuts import render, HttpResponse
import time

#CONTROLLER!!!
# Create your views here.


def index (request):
  context = {
  "date":(time.strftime("%b %d, %Y")),
  "time":(time.strftime("%I:%M:%p"))
  }
  
  return render(request, 'time_display/index.html', context)
  
  
# def show(request):
#   print(request.method)
#   return render (request, 'time_display/show_users.html')
