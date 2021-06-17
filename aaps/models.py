from django.db import models
from enum import Enum
from enumfields import EnumField



class MaritalStatus(Enum):
    MARRIED = 'MARRIED'
    UNMARRIED = 'UNMARRIED'
    WIDOW_MALE = 'WIDOW_MALE'
    WIDOW_FEMALE = 'WIDOW_FEMALE'


class Family(models.Model):
    id = models.AutoField(primary_key=True)
    village_name = models.TextField()
    full_name_english = models.TextField()
    full_name_gujarati = models.TextField()
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
        return "{} ({})".format(self.full_name_gujarati, self.full_name_english)

    class Meta:
        ordering = ['id', 'village_name', 'created_at', 'updated_at', 'created_by', 'modified_by']

