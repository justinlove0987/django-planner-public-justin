# Generated by Django 3.2.8 on 2021-11-14 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_auto_20211022_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learningdetail',
            old_name='every_day_unit',
            new_name='day_unit',
        ),
    ]
