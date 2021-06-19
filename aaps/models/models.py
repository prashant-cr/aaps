from django.db import models
from enum import Enum
from enumfields import EnumField
from django.utils.functional import cached_property


class MaritalStatus(Enum):
    MARRIED = 'MARRIED'
    UNMARRIED = 'UNMARRIED'
    WIDOW_MALE = 'WIDOW_MALE'
    WIDOW_FEMALE = 'WIDOW_FEMALE'


class Villages(Enum):
    ADPODARA = 'અડપોદરા'
    BAKROL = 'બાકરોલ'
    BAMANWAD = 'બામણવાડ'
    BOLUNDRA = 'બોલુન્દ્રા'
    DADHALIYA = 'દધાલીયા'
    DAHEGAMADA = 'દહેગામડા'
    GHADHADA = 'ગઢડા'
    GHADHA = 'ગઢા'
    GADADAR = 'ગડાદર'
    ISARI = 'ઇસરી'
    JITPUR = 'જીતપુર'
    KARCHHA = 'કારછા'
    KUSHKI = 'કુશ્કી'
    KHAMBHISAR = 'ખભીસર'
    KHERANCHA = 'ખેરંચા'
    KHERADI = 'ખેરાડી'
    KHAKHARIYA = 'ખાખરીયા'
    KHODAMBA = 'ખોડંબા'
    LIMBHOI = 'લીંભોઈ'
    LUSADIYA = 'લુસડીયા'
    MALI = 'માળી'
    MEDHASAN = 'મેઢાસણ'
    NAVA = 'નવા'
    NAVAPALLA = 'નવાપાલ્લા'
    NAVAGAM = 'નવાગામ'
    NANDISAN = 'નાદીસણ'
    PEDHMALA = 'પેઢમાળા'
    PALLA = 'પાલ્લા'
    PUJAPUR = 'પુજાપુર'
    RAYGADH = 'રાયગઢ'
    RELLAWADA = 'રેલ્લાવાડા'
    RAKHAPUR = 'રખાપુર'
    SARDOI = 'સરડોઇ'
    SHANGAL = 'શણગાલ'
    TINTOI = 'ટીટોઈ'
    TARAKWADA = 'તરકવાળા'
    VARTHU = 'વરથું'
    VAVKAMPA = 'વાવકંપા'

    def get_name(self):
        return self.name


class Family(models.Model):
    id = models.AutoField(primary_key=True)
    village_name = EnumField(Villages)
    full_name_english = models.TextField(db_index=True)
    full_name_gujarati = models.TextField(db_index=True)
    is_deleted = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({}) - {}".format(self.full_name_gujarati, self.full_name_english, self.village_name.value)

    @cached_property
    def family_members_set(self):
        return FamilyMember.objects.filter(
            family=self
        )

    class Meta:
        ordering = ['id', 'village_name', 'full_name_english', 'created_at']
        verbose_name = 'Main Member'


class FamilyMember(models.Model):
    id = models.AutoField(primary_key=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, db_index=True)
    village_name = EnumField(Villages)
    full_name_english = models.TextField(db_index=True)
    full_name_gujarati = models.TextField(db_index=True)
    is_main_member = models.BooleanField()
    age = models.IntegerField()
    relation_main_member = models.TextField()
    is_engaged = models.BooleanField()
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
        return "{} ({}) - {}".format(self.full_name_gujarati, self.full_name_english, self.village_name.value)

    class Meta:
        ordering = ['id', 'village_name', 'full_name_english', 'created_at']
