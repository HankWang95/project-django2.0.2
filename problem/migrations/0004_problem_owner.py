# Generated by Django 2.0.2 on 2018-05-21 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problem', '0003_auto_20180521_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='problem_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
