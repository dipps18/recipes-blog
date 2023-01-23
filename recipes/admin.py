from django.utils.html import format_html
from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', 'title']

