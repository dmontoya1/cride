"""Circles Admin"""

# Django
from django.contrib import admin

# models
from cride.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """ Circle admin."""
    list_display = (
        'name',
        'slug_name',
        'is_public',
        'verified',
        'is_limited',
        'members_limited'
    )
    search_fields = ('slug_name', 'name')
    list_filter = ('is_public', 'is_limited', 'verified')
