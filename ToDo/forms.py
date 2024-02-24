from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField
from .models import Task, Category


class TaskForm(ModelForm):
    created_by = ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'category', 'priority']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'deleted_at', 'deleted']