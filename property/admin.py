from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)



