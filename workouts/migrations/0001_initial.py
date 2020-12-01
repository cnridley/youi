# Generated by Django 3.1.2 on 2020-12-01 02:15

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
            name='workouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weeks', models.DecimalField(blank=True, decimal_places=0, max_digits=50, null=True)),
                ('body_part', models.CharField(blank=True, max_length=250, null=True)),
                ('exercise', models.CharField(blank=True, max_length=250, null=True)),
                ('reps', models.DecimalField(blank=True, decimal_places=0, max_digits=50, null=True)),
                ('sets', models.DecimalField(blank=True, decimal_places=0, max_digits=50, null=True)),
                ('gym_or_home', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
