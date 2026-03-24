from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'tech_stack')
    search_fields = ('title', 'brief_desc')
    # Superuser can add/edit projects here. Screenshots go to Supabase Storage first, then paste URL
