# Generated by Django 2.1.5 on 2019-02-12 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
