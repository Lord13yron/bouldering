# Generated by Django 5.0.3 on 2024-04-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0016_alter_problem_avgrating_alter_problem_map_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='avggrade',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]