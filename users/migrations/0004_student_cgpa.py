# Generated by Django 5.1 on 2024-09-27 03:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_faculty_email_profile_email_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cgpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
    ]
