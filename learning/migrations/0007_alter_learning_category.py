# Generated by Django 3.2.8 on 2021-11-17 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('learning', '0006_learningdetail_day_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]