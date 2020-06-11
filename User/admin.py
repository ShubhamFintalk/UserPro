from django.contrib import admin

# Register your models here.
from .models import Posts, User


class UserView(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'userName'
    ]


class PostsView(admin.ModelAdmin):
    list_display = [
        'user', 'text', 'created_at', 'updated_at'
    ]


admin.site.register(User, UserView)
admin.site.register(Posts, PostsView)
