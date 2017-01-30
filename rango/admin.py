from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	fields = ['category', 'title', 'url', 'views']
	list_display = ('category', 'title', 'url', 'views')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
