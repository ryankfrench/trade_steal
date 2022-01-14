# Generated by Django 3.2.11 on 2022-01-14 00:24

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0103_rename_invitation_text_subject_parameters_invitation_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='invitation_subject',
            field=tinymce.models.HTMLField(default='', verbose_name='Invitation Subject'),
        ),
    ]
