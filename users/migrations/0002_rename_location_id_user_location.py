# Generated by Django 4.1.6 on 2023-02-14 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location_id',
            new_name='location',
        ),
    ]