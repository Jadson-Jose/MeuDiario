# Generated by Django 5.1.4 on 2025-01-09 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0002_alter_diario_pessoas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diario',
            old_name='tiulo',
            new_name='titulo',
        ),
    ]