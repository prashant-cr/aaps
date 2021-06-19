from django.contrib import admin

from aaps.models import FamilyMember, Family


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(FamilyMember, AuthorAdmin)
admin.site.register(Family, AuthorAdmin)
