# Generated by Django 2.1.1 on 2018-09-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_auto_20180919_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.ImageField(blank='True', upload_to='events'),
        ),
    ]
