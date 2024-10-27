from django.contrib import admin
from .models import Author,SparksModel,Tags , Comment

# Register your models here.

class SparksAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date')
    prepopulated_fields = {('slug') : ('title',)}
    list_display = ('title',  'author', 'date')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',  'email_address')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('username',  'email')


admin.site.register(SparksModel, SparksAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tags)
admin.site.register(Comment, CommentAdmin)