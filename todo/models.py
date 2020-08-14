from django.db import models

# Create your models here.
class Task(models.Model):
  PRIORITY_CHOICES = [
   (3, "High"),
   (2, "Mid"),
   (1, "Low"),
   ]
  name = models.CharField("Task name", max_length = 100)
  completed = models.BooleanField(default = False)
  time_created = models.DateField(auto_now_add = True)
  deadline = models.DateField(blank = True, null = True)
  priority = models.IntegerField(choices = PRIORITY_CHOICES, null = True, blank = True)
  
  def __str__(self):
    return self.name