# Generated by Django 5.0.1 on 2024-02-03 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_is_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_vendor',
            new_name='is_admin',
        ),
    ]
