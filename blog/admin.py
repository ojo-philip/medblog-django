from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted',)
    list_filter = ('title', 'date_posted',)
    search_fields = ('title', 'content',)


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date_posted',)


admin.site.register(Comment, CommentAdmin)
