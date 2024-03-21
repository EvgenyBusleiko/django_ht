from django.contrib import admin
from .models import Author, Post, User
# Register your models here.

# admin.site.register(Author)
# admin.site.register(Post)
# admin.site.register(User)


@admin.register(Author)
class AuthorAdmin (admin.ModelAdmin):
    list_display = ['name',"email","date_of_birth"]
    list_filter = ['name',"date_of_birth"]
    search_fields = ['name__startswith',"email"]
    readonly_fields = ['email']
    list_editable = ["email","date_of_birth"]

@admin.register(Post)
class PostAdmin (admin.ModelAdmin):
    list_display = ['title',"author","date",'views']
    list_filter = ["author","date",'views']
    search_fields = ['title',"author__name"]
    readonly_fields = ['views']
    list_editable = ["author","date"]