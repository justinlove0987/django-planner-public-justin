# Generated by Django 3.2.8 on 2021-11-23 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0022_remove_learning_left_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learning',
            name='progress_percentage',
        ),
    ]