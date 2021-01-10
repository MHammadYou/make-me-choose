# Generated by Django 3.1.4 on 2021-01-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='poll_images'),
        ),
        migrations.AddField(
            model_name='poll',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='poll_images'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
