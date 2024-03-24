from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField
from .models import Task, Category
from django import forms


class TaskForm(ModelForm):
    created_by = ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['created_by', 'title', 'status', 'description']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'deleted_at', 'deleted']
