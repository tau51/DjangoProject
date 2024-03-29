# Generated by Django 4.2.9 on 2024-02-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pj1', '0006_clue_deleted_user_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clue',
            name='wechat',
            field=models.CharField(max_length=32),
        ),
        migrations.AddConstraint(
            model_name='clue',
            constraint=models.UniqueConstraint(fields=('wechat', 'deleted'), name='unique_wechat'),
        ),
        migrations.AddConstraint(
            model_name='clue',
            constraint=models.UniqueConstraint(fields=('club', 'deleted'), name='unique_club'),
        ),
    ]
