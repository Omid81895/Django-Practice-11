from django.contrib import admin
from .models import ToDoList
# Register your models here.
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description', 'created','status']
    ordering = ["created"]
    list_filter = ["created", 'status']
    search_fields = ["name", "created"]
    list_editable = ["status"]
admin.site.register(ToDoList,ToDoListAdmin)