# Generated by Django 3.2.8 on 2021-11-18 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0008_remove_learning_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning',
            name='group_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='learning',
            name='group_order',
            field=models.IntegerField(default=None, unique=True),
        ),
    ]
