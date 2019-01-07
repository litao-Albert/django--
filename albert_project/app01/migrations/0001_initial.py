# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='文章标题', max_length=32)),
                ('time', models.DateTimeField(verbose_name='发表日期')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章描述')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
                ('picture', models.ImageField(verbose_name='文章图片', upload_to='images/article')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, verbose_name='作者姓名', null=True, max_length=32)),
                ('age', models.CharField(blank=True, verbose_name='作者年龄', null=True, max_length=3)),
                ('gender', models.CharField(blank=True, verbose_name='作者性别', null=True, max_length=2, choices=[('M', 'Male'), ('F', 'Female')])),
                ('email', models.CharField(blank=True, verbose_name='作者邮箱', null=True, max_length=32)),
                ('phone', models.CharField(blank=True, verbose_name='作者电话', null=True, max_length=11)),
                ('photo', models.ImageField(verbose_name='作者头像', upload_to='images/author')),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('label', models.CharField(verbose_name='分类标签', max_length=32)),
                ('description', models.TextField(verbose_name='标签描述')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='评论内容')),
                ('content_name', models.CharField(verbose_name='评论用户', max_length=32)),
                ('time', models.DateTimeField(verbose_name='评论时间')),
                ('agree', models.IntegerField(verbose_name='评论点赞')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('label', models.CharField(verbose_name='图片标签', max_length=32)),
                ('image', models.ImageField(verbose_name='图片链接', upload_to='images/picture')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='图片描述')),
                ('classify', models.ForeignKey(verbose_name='图片分类', to='app01.Classify')),
                ('comment', models.ForeignKey(verbose_name='图片评论', to='app01.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='app01.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='clssify',
            field=models.ForeignKey(to='app01.Classify'),
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(to='app01.Comment', blank=True, verbose_name='文章评论', null=True),
        ),
    ]
