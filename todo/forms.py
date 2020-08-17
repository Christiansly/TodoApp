from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'priority', 'deadline']
    widgets = {
      'name': forms.TextInput(attrs = {'class': 'form-control'}),
      'priority': forms.Select(attrs = {'class': 'form-control'}),
      'deadline': forms.SelectDateWidget(attrs = {'class': 'form-control'})
     
      
    }