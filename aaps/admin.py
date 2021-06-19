from django.contrib import admin

from aaps.models import FamilyMember, Family
from django.contrib.auth.admin import UserAdmin


class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'family', 'village_name', 'full_name_english', 'full_name_gujarati', 'is_main_member']
    search_fields = ['id', 'village_name', 'full_name_english', 'full_name_gujarati']

    filter_horizontal = ()


class FamilyAdmin(admin.ModelAdmin):
    list_display = ['id', 'village_name', 'full_name_english', 'full_name_gujarati']
    search_fields = ['id', 'village_name', 'full_name_english', 'full_name_gujarati']

    filter_horizontal = ()



admin.site.register(FamilyMember, FamilyMemberAdmin)
admin.site.register(Family, FamilyAdmin)
