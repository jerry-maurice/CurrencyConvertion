# Generated by Django 2.2 on 2019-06-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferApp', '0002_auto_20190617_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='unitRate',
            field=models.FloatField(default=None),
        ),
    ]