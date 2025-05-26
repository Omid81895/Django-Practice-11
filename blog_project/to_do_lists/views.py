from django.shortcuts import render
from django.http import Http404

# Create your views here.
def todolist(request):
    return render (request,'to_do_lists/main.html')