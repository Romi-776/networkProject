# Generated by Django 3.1.7 on 2021-05-22 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_profile_background_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background_img',
            field=models.ImageField(blank=True, default='Default_background.jpg', null=True, upload_to='bg_img'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
