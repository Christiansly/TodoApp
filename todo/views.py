from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import TaskForm
# Create your views here.
def index(request):
  date = datetime.now()
  tasks = Task.objects.all().filter(completed = False).order_by("-priority")
  context = {"tasks": tasks}
  return render(request, "todo/index.html", context)
  
def completed_tasks(request):
  tasks = Task.objects.all().filter(completed = True).order_by('-time_created')
  context = {"tasks": tasks, "date": date}
  return render(request, "todo/complete.html", context)
  
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
  
def complete_todo(request, task_id):
  task = Task.objects.get(id = task_id)
  task.completed = True
  task.save()
  return HttpResponseRedirect("/")
  
def task_edit(request, task_id):
  task = Task.objects.get(id = task_id)
  submitted = False
  if request.method == 'POST':
    form = TaskForm(instance = task, data = request.POST)
    if form.is_valid():
      form.save()
      submitted = True
  else:
    form = TaskForm(instance = task)
    
  return render(request, 'todo/task_edit.html', {'form': form, 'submitted': submitted})