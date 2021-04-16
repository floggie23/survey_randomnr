from django.shortcuts import render ,HttpResponse,redirect
from django.utils.crypto import get_random_string 
def index(request):
    if request.method == "GET":
    	print("a GET request is being made to this route")
    	return render(request, "index.html")
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST["location"]
        request.session['textt'] = request.POST["textarea"]
        request.session['favlang'] = request.POST["favlang"]
    return redirect('/view')
def index1(request):
    
    return render(request, 'index2.html')
def back(request):
    return redirect('/')



def number(request):
    request.session['number'] = get_random_string(length=14)
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request, "index3.html")
def generate(request):
    request.session['count'] += 1
    request.session['number'] = get_random_string(length=14)
    print(request.session)
    return redirect('/number')
def clear(request):
    request.session.flush()
    return redirect('/number')



