from django.shortcuts import render, redirect, HttpResponse
import random, string
from random import randint
from datetime import datetime

def index (request):
  if 'counter' not in request.session:
    request.session['counter'] = 0
  if 'word' not in request.session:
    request.session['word'] = 'Not Yet Generated Number'
  return render(request, 'random_word/index.html')

def generate(request):
  if 'word' not in request.session:
    request.session['word'] = 'Not Yet Generated Number'
  else:
    randomstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(14))
    request.session['word'] = randomstr
  if 'counter' not in request.session:
    request.session['counter'] = 1
  else:
    request.session['counter'] += 1
  return redirect('/')

# Create your views here.
