# Generated by Django 3.1.2 on 2020-12-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workouts',
            old_name='exercise',
            new_name='exercise1',
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise10',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise4',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise5',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise6',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise7',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise8',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workouts',
            name='exercise9',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]