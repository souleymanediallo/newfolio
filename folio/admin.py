from django.contrib import admin
from .models import Folio

# Register your models here.
@admin.register(Folio)
class FolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
