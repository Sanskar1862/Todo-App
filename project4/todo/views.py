from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    tasks = task.objects.all()


    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks,'form':form}
    return render(request,'todo/list.html',context)


def updateTask(request,pk):
    task1 = task.objects.get(id = pk)
    form = TaskForm(instance=task1)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task1)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'todo/update_task.html',context)

def deleteTask(request,pk):
    item = task.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context={'item':item}
    return render(request,'todo/delete.html',context)
