# Generated by Django 3.1.3 on 2020-11-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_auto_20201126_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]
