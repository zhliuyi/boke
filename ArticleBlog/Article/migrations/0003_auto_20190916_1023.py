# Generated by Django 2.2.1 on 2019-09-16 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0002_auto_20190916_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='data',
            new_name='date',
        ),
    ]
