from django.shortcuts import render, redirect
from .models import Animal

def index(request):
    data={
        'animals': list()
    }
    return render(request,'index.html', data)

def insert(request):
    if request.method=='POST':
        name=request.POST['txt_name']
        details=request.POST['txt_details']
        Animal.objects.create(name=name, details=details)
        return redirect('index')
        

def update(request, id):
    if request.method=='POST':
        name=request.POST['txt_name']
        details=request.POST['txt_details']
        
        Animal.objects.filter(id=id).update(name=name, details=details)
        return redirect('index')
    else:

        data={
            'animal': animal_by_id(id)
        }
        return render(request,'edite.html', data)

def delete(request, id):
    Animal.objects.filter(id=id).delete()
    return redirect('index')

def animal_by_id(id):
    return Animal.objects.get(id=id)
def list():
    animals=Animal.objects.all()
    return animals   
