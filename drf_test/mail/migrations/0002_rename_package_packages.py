# Generated by Django 5.0.2 on 2024-02-20 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Package',
            new_name='Packages',
        ),
    ]
