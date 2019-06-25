# Generated by Django 2.2 on 2019-06-17 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transfer_comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transfer_givenAmount',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transfer_originAmount',
            field=models.FloatField(default=None),
        ),
    ]
