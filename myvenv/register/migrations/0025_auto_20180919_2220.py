# Generated by Django 2.1.1 on 2018-09-19 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0024_auto_20180919_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='comp_allowed',
            new_name='allowed',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='comp_reported',
            new_name='reported',
        ),
    ]
