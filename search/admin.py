from django.contrib import admin

# Register your models here.
from .models import Chapter, Verse

admin.site.register(Chapter)
admin.site.register(Verse)
