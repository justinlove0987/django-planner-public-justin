# Generated by Django 3.2.8 on 2021-10-20 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_learning_progress_percentage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learningdetail',
            old_name='date',
            new_name='expired_datetime',
        ),
    ]
