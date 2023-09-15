# Generated by Django 4.2.5 on 2023-09-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Callsign', models.CharField(max_length=15)),
                ('Taxi', models.JSONField(null=True)),
                ('Takeoff', models.CharField(max_length=10, null=True)),
                ('Landing', models.CharField(max_length=10, null=True)),
                ('lastInstruction', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]