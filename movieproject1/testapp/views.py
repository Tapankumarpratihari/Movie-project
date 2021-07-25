from django import forms
from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import Movie

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def addmovies_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home_view(request)
    return render(request,'testapp/addmovies.html',{'form':form})

def listmovies_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/listmovies.html',{'movies_list':movies_list})