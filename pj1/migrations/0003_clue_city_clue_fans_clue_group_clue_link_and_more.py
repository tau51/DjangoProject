# Generated by Django 4.2.9 on 2024-02-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pj1', '0002_user_remove_clue_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='city',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='clue',
            name='fans',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clue',
            name='group',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clue',
            name='link',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clue',
            name='province',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='clue',
            name='type',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clue',
            name='club',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='clue',
            name='note',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='clue',
            name='wechat',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]