# Generated by Django 5.0.3 on 2024-03-31 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0011_alter_rating_user_grade_alter_rating_user_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='problem',
            new_name='problem_name',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='user',
            new_name='user_name',
        ),
    ]