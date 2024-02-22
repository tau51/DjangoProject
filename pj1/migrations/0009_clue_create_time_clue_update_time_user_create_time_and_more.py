# Generated by Django 4.2.9 on 2024-02-19 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pj1', '0008_alter_clue_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clue',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
