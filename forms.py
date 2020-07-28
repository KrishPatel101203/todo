from django.forms import ModelForm
from .models import Tasks
from django import forms

class TasksCreation(ModelForm):
    title = forms.CharField(label='new Task',widget=forms.TextInput (attrs={'placeholder':'add tasks'}))
    class Meta:
        model= Tasks
        fields = ['title']

class TaskUpdate(ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'