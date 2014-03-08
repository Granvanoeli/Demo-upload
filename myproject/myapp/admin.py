from django.contrib import admin
from myproject.myapp.models import Document


class PageAdmin(admin.ModelAdmin):
    list_display = ('user', 'docfile', 'title', 'genre', 'img', 'up', 'down')

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('image',)

admin.site.register(Document, PageAdmin)
# admin.site.register(Image, ImageAdmin)
