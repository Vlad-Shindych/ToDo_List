from django.contrib import admin

from ToDo.models import Task, Category, Priority

# Register your models here.
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Priority)