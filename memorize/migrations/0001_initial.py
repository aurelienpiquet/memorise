# Generated by Django 3.2.7 on 2021-10-04 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='titre')),
                ('color', models.CharField(max_length=255, verbose_name='couleur')),
                ('thumbnail', models.ImageField(max_length=255, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phoen', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Todolist')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Sous-titre')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('remind', models.BooleanField(default=False)),
                ('checked', models.BooleanField(default=False, verbose_name='checked')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='memorize.category', verbose_name='categorie')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
        ),
    ]
