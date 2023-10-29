from django.contrib import admin
from .models import Language

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'knowledge', 'description')
    prepopulated_fields = {'slug':('language','knowledge')}
admin.site.register(Language, LanguageAdmin)