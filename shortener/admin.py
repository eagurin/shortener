from django.contrib import admin

from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ("url", "shorten", "count", "pub_date")
    empty_value_display = "-пусто-"
