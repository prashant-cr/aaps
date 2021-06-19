from rest_framework import serializers
from django.db import transaction
from aaps.models import Family
from enumfields.drf.fields import EnumField as EnumSerializerFiled
from .models import MaritalStatus, FamilyMember, Family, Villages, Engaged


class FamilyMembersSerializer(serializers.ModelSerializer):
    marital_status = EnumSerializerFiled(MaritalStatus, required=False)
    village_name = EnumSerializerFiled(Villages)
    mobile_numbers = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    business_Occupation = serializers.CharField(required=False)
    education = serializers.CharField(required=False)
    father_name_village = serializers.CharField(required=False)
    is_engaged = EnumSerializerFiled(Engaged)

    class Meta:
        model = FamilyMember
        fields = ['id', 'village_name', 'family', 'full_name_english', 'full_name_gujarati', 'is_main_member', 'age', 'relation_main_member',
                  'marital_status', 'is_engaged', 'education', 'business_Occupation', 'father_name_village', 'address', 'mobile_numbers',
                   'created_at', 'updated_at']


class FamilySerializer(serializers.ModelSerializer):
    # family_members = serializers.ListSerializer(
    #     child=serializers.PrimaryKeyRelatedField(queryset=FamilyMember.objects.all()), read_only=True)

    # family_members = serializers.ListField(child=FamilyMembersSerializer(Family.family_members_set, many=True), read_only=True, allow_null=True)
    family_members = serializers.SerializerMethodField('_get_children', allow_null=True)
    village_name = EnumSerializerFiled(Villages)

    def _get_children(self, obj):
        serializer = FamilyMembersSerializer(obj.family_members_set.all(), many=True)
        return serializer.data

    class Meta:
        model = Family
        fields = ['id', 'village_name', 'full_name_english', 'full_name_gujarati', 'family_members']




    # def create(self, validated_data):
    #
    #     try:
    #         with transaction.atomic():
    #             is_main_member = validated_data.get('is_main_member')
    #             if is_main_member:
    #                 f_data = {
    #                     'village_name': validated_data.get('village_name'),
    #                     'full_name_english': validated_data.get('full_name_english'),
    #                     'full_name_gujarati': validated_data.get('full_name_gujarati')
    #                 }
    #                 fm_data = Family.objects.create(**f_data)
    #
    #                 validated_data['family'] = fm_data
    #
    #             family_data = FamilyMember.objects.create(**validated_data)
    #
    #             return family_data
    #
    #     except Exception as e:
    #         pass




