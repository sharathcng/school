# Generated by Django 3.2.9 on 2021-12-15 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('assessments', '0006_alter_assessment_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assessment',
            unique_together={('class_name', 'subject', 'assessment_type')},
        ),
    ]
