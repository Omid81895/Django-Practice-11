from django.shortcuts import render
from django.http import Http404
from .models import ToDoList
from .form import ToDoListForm
import datetime as dt
# Create your views here.
def todolist(request):
    tasks = ToDoList.objects.all()
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