from django.forms import ModelForm
from todolist.models import Task

class CreateNewTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']