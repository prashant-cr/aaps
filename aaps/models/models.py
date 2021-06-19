from django.db import models
from enum import Enum
from enumfields import EnumField
from django.utils.functional import cached_property


class MaritalStatus(Enum):
    MARRIED = 'MARRIED'
    UNMARRIED = 'UNMARRIED'
    WIDOW_MALE = 'WIDOW_MALE'
    WIDOW_FEMALE = 'WIDOW_FEMALE'


class Family(models.Model):
    id = models.AutoField(primary_key=True)
    village_name = models.TextField()
    full_name_english = models.TextField(db_index=True)
    full_name_gujarati = models.TextField(db_index=True)
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({}) - {}".format(self.full_name_gujarati, self.full_name_english, self.village_name)

    @cached_property
    def family_members_set(self):
        return FamilyMember.objects.filter(
            family=self
        )

    class Meta:
        ordering = ['id', 'village_name', 'full_name_english', 'created_at']


class FamilyMember(models.Model):
    id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, db_index=True)
    village_name = models.TextField(db_index=True)
    full_name_english = models.TextField(db_index=True)
    full_name_gujarati = models.TextField(db_index=True)
    is_main_member = models.BooleanField()
    age = models.IntegerField()
    relation_main_member = models.TextField()
    marital_status = EnumField(MaritalStatus)
    education = models.TextField()
    business_Occupation = models.TextField()
    father_name_village = models.TextField()
    address = models.TextField()
    mobile_numbers = models.TextField()
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({}) - {}".format(self.full_name_gujarati, self.full_name_english, self.village_name)

    class Meta:
        ordering = ['id', 'village_name', 'full_name_english', 'created_at']
