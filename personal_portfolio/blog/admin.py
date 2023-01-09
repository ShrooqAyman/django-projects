from django.contrib import admin
from blog import models

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)


