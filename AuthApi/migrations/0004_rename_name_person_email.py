# Generated by Django 3.2.8 on 2021-10-18 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApi', '0003_auto_20211018_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='email',
        ),
    ]
