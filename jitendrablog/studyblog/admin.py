from django.contrib import admin
from .models import Studyblog
# Register your models here.
class StudyblogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'list_date', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_per_page = 25

admin.site.register(Studyblog, StudyblogAdmin)