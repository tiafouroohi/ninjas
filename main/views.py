from django.shortcuts import render, HttpResponse, redirect
from . models import Dojo, Ninja

def index(request):
    all_dojo = Dojo.objects.all()
    all_ninja = Ninja.objects.all()
    context = {
        "all_dojo": all_dojo,
        "all_ninja": all_ninja,
    }
    return render (request, "index.html", context)

def process(request):
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
    )
    return redirect ("/")

def other(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = Dojo.objects.get(id=request.POST['dojo']),
    )
    return redirect ("/")
# Create your views here.


