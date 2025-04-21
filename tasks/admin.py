from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'completed')
    list_filter = ('completed', 'created_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'
