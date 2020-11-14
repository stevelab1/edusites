from django.contrib import admin
from .models import Profile




admin.site.site_header = "FictionPy"
admin.site.index_title = "Admin"
admin.site.site_title = "FictionPy"

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
