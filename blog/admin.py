from django.contrib import admin
from .models import Artist, Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'category', 'is_favourite')
    list_filter = ('category', 'is_favourite')

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'language')  # Fixed the 'langauge' typo
    list_filter = ('language',)  # Added a comma to make it a tuple

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
