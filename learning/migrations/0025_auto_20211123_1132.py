# Generated by Django 3.2.8 on 2021-11-23 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0024_auto_20211123_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learning',
            name='learning_detail',
        ),
        migrations.AddField(
            model_name='learningdetail',
            name='learning',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.learning'),
        ),
    ]