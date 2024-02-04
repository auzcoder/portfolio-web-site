from django.contrib import admin

from aloqa.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'email', 'created_at']
