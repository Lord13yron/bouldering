# Generated by Django 5.0.3 on 2024-04-02 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0014_problem_avgrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='avgrating',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
    ]
