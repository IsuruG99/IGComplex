from django.contrib import admin
from .models import Image 

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'tags')
    search_fields = ('tags',)
    ordering = ('-date',)    # Superuser can add/edit projects here. Screenshots go to Supabase Storage first, then paste URL
