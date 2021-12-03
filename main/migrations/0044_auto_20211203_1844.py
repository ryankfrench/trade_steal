# Generated by Django 3.2.8 on 2021-12-03 18:44

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_sessionplayer_earnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionplayer',
            name='good_one_production_rate',
            field=models.IntegerField(default=50, verbose_name='Good one production rate (0-100)'),
        ),
        migrations.AddField(
            model_name='sessionplayer',
            name='good_two_production_rate',
            field=models.IntegerField(default=50, verbose_name='Good two production rate (0-100)'),
        ),
        migrations.AddConstraint(
            model_name='sessionplayer',
            constraint=models.CheckConstraint(check=django.db.models.expressions.RawSQL('good_one_production_rate+good_two_production_rate=100', (), output_field=models.BooleanField()), name='production_total_equals_100'),
        ),
    ]
