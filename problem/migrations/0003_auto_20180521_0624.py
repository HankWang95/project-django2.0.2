# Generated by Django 2.0.2 on 2018-05-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_problem_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='series',
            field=models.IntegerField(verbose_name='series_id'),
        ),
    ]
