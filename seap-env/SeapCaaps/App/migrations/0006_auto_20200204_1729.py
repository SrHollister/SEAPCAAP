# Generated by Django 2.2.7 on 2020-02-04 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20200128_0245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antrecreathab',
            old_name='Drogradiccion',
            new_name='Drogadiccion',
        ),
        migrations.RenameField(
            model_name='personalidad',
            old_name='Obs_ConsidFelidicad',
            new_name='Obs_ConsidFelicidad',
        ),
    ]