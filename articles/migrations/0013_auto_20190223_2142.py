# Generated by Django 2.1.7 on 2019-02-23 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20190223_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='articless',
        ),
    ]