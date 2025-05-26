from django.shortcuts import render
from django.http import Http404
from .models import ToDoList
from .form import ToDoListForm
# Create your views here.
def todolist(request):
    tasks = ToDoList.objects.all()
    return render (request,'to_do_lists/main.html', {'tasks': tasks})
def add(request):
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cd['name']
    else:
        form = ToDoList()
    return render (request,'to_do_lists/add.html',{'form':form})