from django.utils.html import format_html
from django.contrib import admin
from .models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', 'title']


class CommentInline(admin.StackedInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,
               ]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)

