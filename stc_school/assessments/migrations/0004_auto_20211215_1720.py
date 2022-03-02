# Generated by Django 3.2.9 on 2021-12-15 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('assessments', '0003_alter_assessment_type_assessment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='class_name',
        ),
        migrations.AddField(
            model_name='result',
            name='class_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.class_list'),
            preserve_default=False,
        ),
    ]
