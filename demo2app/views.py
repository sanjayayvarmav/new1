from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import MovieForm

# Create your views here.
def index(request):
    result=movie.objects.all()


    return render(request,'index.html',{'show':result})
def details(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'mov':mov})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()
    return render(request,'add.html')
def update(request,id):
    mov=movie.objects.get(id=id)
    frm=MovieForm(request.POST or None,request.FILES,instance=mov)
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request,'update.html',{'form':frm,'mov':mov})
def delete(request,id):
    mov=movie.objects.get(id=id)
    if request.method=='POST':
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')