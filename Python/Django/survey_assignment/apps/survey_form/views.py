from django.shortcuts import render, redirect, HttpResponse

def index(request):
  return render(request, 'survey_form/index.html')
  
def process(request):
  print "YOOOOOOOO"
  if 'counter' not in request.session:
    request.session['counter'] = 1

  request.session['name'] = request.POST['name']
  request.session['location'] = request.POST['location']
  request.session['language'] = request.POST['language']
  request.session['comment'] = request.POST['comment']
  request.session['counter'] += 1
  return redirect('/results')

def results(request):
  return render(request, 'survey_form/results.html')
  
# def go_back(request):
#     return redirect('/')
# Create your views here.
