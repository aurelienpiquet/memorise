# Generated by Django 3.2.7 on 2021-10-04 10:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('phoneNumber', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Téléphone')),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Utilisateur',
            },
        ),
    ]
