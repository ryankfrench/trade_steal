# Generated by Django 3.2.9 on 2022-01-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0085_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='text',
            field=models.CharField(default='Chat here', max_length=100000, verbose_name='Page Text'),
        ),
    ]
