from . import views
from django.urls import path
urlpatterns = [
  path("", views.index, name = "index"),
  path("add_todo/", views.add_task, name = "add"),
  path("delete_todo/<int:task_id>", views.delete_todo, name = "delete"),
  path("complete/<int:task_id>", views.complete_todo, name = 'complete'),
  path("completed_tasks/", views.completed_tasks, name = 'completed_tasks'),
  path("edit/<int:task_id>", views.task_edit, name = "edit")
  ]