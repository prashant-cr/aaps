from django.contrib import admin

from aaps.models import Family


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Family, AuthorAdmin)
