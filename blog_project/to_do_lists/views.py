from django.shortcuts import render,redirect
from django.http import Http404
from .models import ToDoList
from .form import ToDoListForm
import datetime as dt
# Create your views here.
def todolist(request):
    tasks = ToDoList.objects.all().order_by('-id')
    return render (request,'to_do_lists/main.html', {'tasks': tasks})
def add(request):
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            task = ToDoList(name = name, description = description,created = dt.datetime.now(), status = status)
            task.save()
    else:
        form = ToDoList()
    return render (request,'to_do_lists/add.html',{'form':form})
def change(request, id):
    task = ToDoList.objects.get(id=id)
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            task.name = cd['name']
            task.description = cd['description']
            task.status = cd['status']
            task.save()
            return redirect('home')
    else:
        form = ToDoListForm(initial= {'name' : task.name,
                                        'description': task.description,
                                        'status': task.status,
                                        'created': task.created})
    return render (request,'to_do_lists/change.html',{'form':form})

def delete(request,id):
    task = ToDoList.objects.get(id=id)
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            task.name = cd['name']
            task.description = cd['description']
            task.status = cd['status']
            task.delete()
            return redirect('home')
    else:
        form = ToDoListForm(initial= {'name' : task.name,
                                        'description': task.description,
                                        'status': task.status,
                                        'created': task.created})
    return render (request,'to_do_lists/delete.html',{'form':form})