from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateField(auto_now=True)
    status = models.BooleanField()
    def __str__(self):
        return self.name