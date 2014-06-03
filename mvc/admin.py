'''
Created on 2013-4-11

@author: computer
'''
from mvc.models import Book
from mvc.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class BookAdmin(admin.ModelAdmin):
#     fields = ['name', 'pub_date']
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date admin', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'
    
admin.site.register(Book, BookAdmin)