from django.contrib import admin

from .models import Articles, Tags, Editor


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('Tags',)


admin.site.register(Editor)
admin.site.register(Articles, ArticleAdmin)
admin.site.register(Tags)
