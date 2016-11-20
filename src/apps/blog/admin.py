from django.contrib import admin
from blog.models import Post


class Admin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['headline', 'text']}),
        ('Информация', {'fields': ['date', 'author'],
                        'classes': ['collapse']}),
    ]


admin.site.register(Post, Admin)
