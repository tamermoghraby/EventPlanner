# Generated by Django 4.0.4 on 2022-06-02 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='event',
        ),
    ]