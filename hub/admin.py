from django.contrib import admin
from .models import Gacha 

@admin.register(Gacha)
class HubAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'pity_num_lim', 'pity_max_std')
    search_fields = ('title', 'year')
    # Superuser can add/edit projects here. Screenshots go to Supabase Storage first, then paste URL
