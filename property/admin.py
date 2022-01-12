from django.contrib import admin

from .models import Flat, Complain


@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)