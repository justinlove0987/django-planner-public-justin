# Generated by Django 3.2.8 on 2021-11-23 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0021_alter_learning_learning_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learning',
            name='left_unit',
        ),
    ]
