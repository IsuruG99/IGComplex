from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'created_at')
    search_fields = ('id', 'title', 'description')
    list_filter = ('start_date', 'end_date', 'created_at')
    date_hierarchy = 'start_date'
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Content', {'fields': ('title', 'description')}),
        ('Dates', {'fields': ('start_date', 'end_date')}),
        ('Images', {'fields': ('image_1', 'image_2', 'image_3')}),
        ('Metadata', {'fields': ('created_at',)}),
    )
