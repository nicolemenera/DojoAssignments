from django.shortcuts import render
  # CONTROLLER
  # Create your views here.
def index(request):
  print "Hello, I am your first request!"
  return render(request, "shmoople/index.html")
  
def show(request):
  print(request.method)
  return render(request, 'shmoople/show_user')
  
def create(request):
  print(request.method)
  if request.method == "POST":
    print "WHAAATS UUUUPPPP"
    request.session['name'] = request.POST['first_name']
    return redirect('/')
  else:
    return redirect('/')
