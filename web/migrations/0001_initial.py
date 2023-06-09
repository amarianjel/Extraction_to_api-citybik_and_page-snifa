# Generated by Django 4.2.1 on 2023-06-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('contador', models.IntegerField()),
                ('empty_slots', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('free_bikes', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('normal_bikes', models.IntegerField()),
                ('payment', models.CharField(max_length=255)),
            ],
        ),
    ]
