# Generated by Django 2.0.2 on 2018-05-19 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0012_auto_20180518_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='img',
            field=models.FilePathField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Series_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='series',
            name='tag',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='输入关键字，使用空格分割'),
        ),
    ]
