# Generated by Django 4.0 on 2022-01-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='aftrn_presence',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='morng_presence',
            field=models.BooleanField(default=True),
        ),
    ]
