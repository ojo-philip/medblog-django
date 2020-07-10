from django.contrib import admin
from .models import UserProfile, SearchQuery


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name',)
    search_fields = ('last_name', 'first_name',)


admin.site.register(UserProfile, UserAdmin)


class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('query', 'timestamp')
    list_filter = ('query', 'timestamp',)
    search_fields = ('query',)


admin.site.register(SearchQuery, SearchQueryAdmin)
