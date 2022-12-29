from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse 
# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add Task",min_length=8,required=True)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request , 'task/index.html',{"tasks":request.session["tasks"]})

def add(request):
    if request.method=="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"task/addTask.html",{"form":form})
    return render(request, 'task/addTask.html',{'form':NewTaskForm()})