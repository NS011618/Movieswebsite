# Generated by Django 4.0.5 on 2022-06-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mshow',
            name='mimage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
