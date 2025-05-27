from django import forms
class ToDoListForm(forms.Form):
    name = forms.CharField(max_length=250)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.BooleanField(label='Complete?', required=False)