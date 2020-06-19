# Generated by Django 3.0.3 on 2020-06-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_profile_dbs'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='area',
            field=models.CharField(choices=[('AE', 'A&E Nurse'), ('DR', 'Doctor')], default='Blank', max_length=2),
        ),
    ]