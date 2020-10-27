# Generated by Django 3.1.2 on 2020-10-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
