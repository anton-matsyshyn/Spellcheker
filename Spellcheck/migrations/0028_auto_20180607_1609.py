# Generated by Django 2.0.5 on 2018-06-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spellcheck', '0027_auto_20180607_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='dateTimeCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='dateTimeDelete',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]