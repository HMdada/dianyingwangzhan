from django.contrib import admin
from .models import Text
class TextInfoAdmin(admin.ModelAdmin):
	list_display = ("text",)

admin.site.register(Text,TextInfoAdmin)