# Generated by Django 3.2.7 on 2021-09-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0004_auto_20210930_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='checkbox_3',
            field=models.CharField(default='checked', max_length=10),
        ),
    ]