# Generated by Django 2.0.5 on 2018-06-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spellcheck', '0028_auto_20180607_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='dateTimeCreated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='text',
            name='dateTimeDelete',
            field=models.DateTimeField(),
        ),
    ]