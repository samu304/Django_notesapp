from django.contrib import admin
from .models import Note

# uername = samu123
# password = samundra

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display =['id','title','text','time']