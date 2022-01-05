# Generated by Django 3.2.9 on 2022-01-04 17:23

from django.db import migrations, models
import django.db.models.deletion

from main.models import InstructionSet

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0090_remove_instruction_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructionSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Name Here', max_length=100, verbose_name='Label')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Instruction Set',
                'verbose_name_plural': 'Instruction Sets',
                'ordering': ['label'],
            },
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='label',
        ),
        migrations.AddConstraint(
            model_name='instructionset',
            constraint=models.UniqueConstraint(fields=('label',), name='unique_instruction_set'),
        ),
    ]
