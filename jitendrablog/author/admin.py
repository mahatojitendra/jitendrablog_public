from django.contrib import admin
from .models import Author
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'join_date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 25

admin.site.register(Author, AuthorAdmin)