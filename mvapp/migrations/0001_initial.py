# Generated by Django 4.0.5 on 2022-06-19 02:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mshow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Moviename', models.CharField(max_length=150)),
                ('Heroname', models.CharField(max_length=150)),
                ('Heroiename', models.CharField(max_length=150)),
                ('Director', models.CharField(max_length=150)),
                ('Releasedate', models.DateField(default=None)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('image', models.URLField(max_length=1000)),
            ],
        ),
    ]