# Generated by Django 5.0.3 on 2024-03-31 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0009_ratings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
    ]