# Generated by Django 3.2.9 on 2021-12-04 09:48

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.PositiveIntegerField(choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Staff')], null=True)),
                ('is_classTeacher', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser')),
                ('full_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True)),
                ('place_of_birth', models.CharField(max_length=255)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], null=True)),
                ('email_id', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('blood_group', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('Not Sure', 'Not Sure')], max_length=10, null=True)),
                ('aadhaar_number', models.CharField(max_length=12)),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('profile_pic', models.ImageField(upload_to=None)),
                ('started_class', models.CharField(max_length=255)),
                ('current_class', models.CharField(max_length=255)),
                ('joining_date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser')),
                ('full_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], null=True)),
                ('email_id', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('blood_group', models.IntegerField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('Not Sure', 'Not Sure')], null=True)),
                ('aadhaar_number', models.CharField(max_length=255)),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('profile_pic', models.ImageField(upload_to=None)),
                ('started_date', models.DateField(null=True)),
                ('handling_subjects', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parents_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('father_occupation', models.CharField(max_length=255)),
                ('mother_occupation', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=255)),
                ('father_qualification', models.CharField(max_length=255)),
                ('mother_qualification', models.CharField(max_length=255)),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
    ]