# Generated by Django 2.2 on 2019-04-02 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlmodel',
            name='shortened_url',
        ),
    ]
