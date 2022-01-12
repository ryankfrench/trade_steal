# Generated by Django 3.2.11 on 2022-01-12 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0097_sessionplayernotice_show_on_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameters',
            name='channel_key',
        ),
        migrations.AddField(
            model_name='parameters',
            name='avatar_sprite_sheet',
            field=models.CharField(default='avatars.json', max_length=200),
        ),
        migrations.AddField(
            model_name='parameters',
            name='graph_sprite_sheet',
            field=models.CharField(default='sprite_sheet.json', max_length=200),
        ),
    ]
