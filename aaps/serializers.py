from rest_framework import serializers
from aaps.models import Family
from enumfields.drf.fields import EnumField as EnumSerializerFiled
from .models import MaritalStatus


class FamilySerializer(serializers.HyperlinkedModelSerializer):
    marital_status = EnumSerializerFiled(MaritalStatus)

    class Meta:
        model = Family
        fields = ['id', 'village_name', 'full_name_english', 'full_name_gujarati', 'is_main_member', 'age', 'relation_main_member',
                  'marital_status', 'education', 'business_Occupation', 'father_name_village', 'address', 'mobile_numbers',
                   'created_at', 'updated_at']
