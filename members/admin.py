from django.contrib import admin
from . import models

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'joined_date']
    prepopulated_fields  = {'slug': ['firstname', 'lastname']}
admin.site.register(models.Member, MemberAdmin)