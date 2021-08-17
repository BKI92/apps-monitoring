from django.contrib import admin
from .models import AppLog, App


@admin.register(AppLog)
class AppLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'app_id', 'created')
    search_fields = ('id', 'app_id', 'created')
    list_filter = ('created',)
    empty_value_display = '-пусто-'


@admin.register(App)
class AppLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'app_id', )
    search_fields = ('id', 'app_id', )
    empty_value_display = '-пусто-'