# Generated by Django 4.2.9 on 2024-02-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pj1', '0005_alter_clue_audits_alter_clue_settle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
