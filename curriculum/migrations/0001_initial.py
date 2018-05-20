# Generated by Django 2.0.2 on 2018-05-20 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300, verbose_name='正文')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否显示')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculum.Comment', verbose_name='上级评论')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['-created_time'],
                'get_latest_by': 'created_time',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('file_name', models.CharField(max_length=50)),
                ('path', models.FilePathField()),
                ('number', models.IntegerField(verbose_name='集数')),
                ('attachment', models.FilePathField()),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Curriculum_editor', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Curriculum_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CurriculumParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='KindOfSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('parent_kind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curriculum.KindOfSeries')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number_of_participants', models.IntegerField(default=0, verbose_name='参加课程人数')),
                ('checked', models.BooleanField(default=False)),
                ('introduce', models.CharField(blank=True, max_length=200, null=True, verbose_name='系列简介')),
                ('tag', models.CharField(blank=True, max_length=50, null=True, verbose_name='输入关键字，使用空格分割')),
                ('img', models.FilePathField(blank=True, null=True)),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Series_kind', to='curriculum.KindOfSeries', verbose_name='所属类型')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Series_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnauditedCurriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('path', models.FilePathField()),
                ('number', models.IntegerField(verbose_name='集数')),
                ('attachment', models.FilePathField(blank=True, null=True, verbose_name='附件文件')),
                ('checked', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UnauditedCurriculum_owner', to=settings.AUTH_USER_MODEL)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UnauditedCurriculum_series', to='curriculum.Series')),
            ],
            options={
                'ordering': ['number'],
                'permissions': (('upload_file', '可以上传文件'), ('editor', '审核员权限')),
            },
        ),
        migrations.CreateModel(
            name='UnPassCurriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UnPassCurriculum_curriculum', to='curriculum.UnauditedCurriculum')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UnPassCurriculum_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='curriculumparticipation',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.Series'),
        ),
        migrations.AddField(
            model_name='curriculumparticipation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Curriculum_series', to='curriculum.Series'),
        ),
        migrations.AddField(
            model_name='comment',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment_series', to='curriculum.Series'),
        ),
    ]
