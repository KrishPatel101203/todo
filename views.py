from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Tasks
from .forms import TasksCreation, TaskUpdate

def index(request):
    form = TasksCreation()
    tasks = Tasks.objects.all()

    if request.method=='POST':
        form = TasksCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'items':tasks, 'forms':form}

    return render(request,'tasks/index.html',context)

def Update_task(request,id):
    task = Tasks.objects.get(id=id)
    form = TaskUpdate(instance=task)
    context = {'task':task, 'form':form}

    if request.method=='POST':
        form = TaskUpdate(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'tasks/update_task.html',context)

def delete_task(request,id):
    task = Tasks.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    context = {'task':task}
    return render(request,'tasks/delete_task.html',context)

