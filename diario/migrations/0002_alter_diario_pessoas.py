# Generated by Django 5.1.4 on 2025-01-09 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='pessoas',
            field=models.ManyToManyField(blank=True, null=True, to='diario.pessoa'),
        ),
    ]
