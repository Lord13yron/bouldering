# Generated by Django 5.0.3 on 2024-03-30 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_remove_zone_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('map', models.ImageField(null=True, upload_to='')),
                ('approach', models.TextField(blank=True, null=True)),
                ('best_problems', models.CharField(blank=True, max_length=200, null=True)),
                ('zone', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='guide.zone')),
            ],
        ),
    ]
