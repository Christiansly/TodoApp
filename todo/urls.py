from . import views
from django.urls import path
urlpatterns = [
  path("", views.index, name = "index"),
  path("add_todo/", views.add_task, name = "add"),
  path("delete_todo/<int:task_id>", views.delete_todo, name = "delete"),
  ]