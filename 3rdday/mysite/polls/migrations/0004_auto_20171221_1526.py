# Generated by Django 2.0 on 2017-12-21 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20171221_1510'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Message',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
