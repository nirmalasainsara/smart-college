from django.contrib import admin
from .models import Category, Year, Subject, Paper, Notes_file, Video_url, Material

admin.site.register(Category)
admin.site.register(Year)
admin.site.register(Subject)
admin.site.register(Paper)
admin.site.register(Notes_file)
admin.site.register(Video_url)
admin.site.register(Material)

# Register your models here.
