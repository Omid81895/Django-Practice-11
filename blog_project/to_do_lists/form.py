from django import forms
from django.core import validators
class ToDoListForm(forms.Form):
    name = forms.CharField(max_length=250, label='task name',
                           widget=forms.TextInput({'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea({'class': 'form-control'}))
    status = forms.BooleanField(label='Complete?', required=False)