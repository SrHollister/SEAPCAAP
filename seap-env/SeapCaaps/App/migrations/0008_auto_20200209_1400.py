# Generated by Django 2.2.7 on 2020-02-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20200209_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoraciontanner',
            name='Img_ValTanner',
            field=models.ImageField(null=True, upload_to='images/EVtanner'),
        ),
    ]
