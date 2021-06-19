# Generated by Django 3.2.4 on 2021-06-19 15:12

import aaps.models.models
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('village_name', enumfields.fields.EnumField(enum=aaps.models.models.Villages, max_length=10)),
                ('full_name_english', models.TextField(db_index=True)),
                ('full_name_gujarati', models.TextField(db_index=True)),
                ('is_deleted', models.BooleanField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
                ('modified_by', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Main Member',
                'ordering': ['id', 'village_name', 'full_name_english', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('village_name', enumfields.fields.EnumField(enum=aaps.models.models.Villages, max_length=10)),
                ('full_name_english', models.TextField(db_index=True)),
                ('full_name_gujarati', models.TextField(db_index=True)),
                ('is_main_member', models.BooleanField()),
                ('age', models.IntegerField()),
                ('relation_main_member', models.TextField()),
                ('is_engaged', enumfields.fields.EnumField(enum=aaps.models.models.Engaged, max_length=10)),
                ('marital_status', enumfields.fields.EnumField(enum=aaps.models.models.MaritalStatus, max_length=10)),
                ('education', models.TextField()),
                ('business_Occupation', models.TextField()),
                ('father_name_village', models.TextField()),
                ('address', models.TextField()),
                ('mobile_numbers', models.TextField()),
                ('is_deleted', models.BooleanField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
                ('modified_by', models.CharField(max_length=100)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aaps.family')),
            ],
            options={
                'ordering': ['id', 'village_name', 'full_name_english', 'created_at'],
            },
        ),
    ]
