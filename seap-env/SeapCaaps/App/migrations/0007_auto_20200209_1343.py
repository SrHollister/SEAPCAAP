# Generated by Django 2.2.7 on 2020-02-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20200204_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='valoraciontanner',
            name='DescripcionValTanner',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='valoraciontanner',
            name='NombreValTanner',
            field=models.CharField(max_length=50),
        ),
    ]
