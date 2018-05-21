# Generated by Django 2.0.2 on 2018-05-21 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_auto_20180520_0748'),
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='problem', to='curriculum.Series'),
            preserve_default=False,
        ),
    ]
