# Generated by Django 3.2.8 on 2021-11-22 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0020_learning_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='learning_name',
            field=models.CharField(max_length=100),
        ),
    ]
