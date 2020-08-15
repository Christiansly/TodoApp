from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from datetime import datetime
# Create your views here.
def index(request):
  tasks = Task.objects.all().filter(completed = False).order_by("-priority")
  context = {"tasks": tasks}
  return render(request, "todo/index.html", context)
  
def add_task(request):
  task_name = request.POST["task_name"]
  task_deadline = request.POST["deadline"][2:]
  task_priority = 1
  if request.POST["priority"] == "High":
    task_priority = 3  
  elif request.POST["priority"] == "Mid" :
    task_priority = 2 
  else: 
    task_priority = 1
  time = datetime.strptime(task_deadline, '%y-%m-%d')
  
  task = Task.objects.create(name = task_name, deadline = time, priority = task_priority)
  return HttpResponseRedirect("/")
  
def delete_todo(request, task_id):
  Task.objects.get(id = task_id).delete()
  return HttpResponseRedirect("/")