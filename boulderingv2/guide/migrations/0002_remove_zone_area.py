# Generated by Django 5.0.3 on 2024-03-30 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='area',
        ),
    ]