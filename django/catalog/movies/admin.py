from django.contrib import admin
from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_date', 'isPublished')
    list_display_links = ('id','name')
    list_filter = ('create_date',)
    list_editable = ('isPublished',)
    search_fields = ('name', 'description',)

admin.site.register(Movie, MovieAdmin)
