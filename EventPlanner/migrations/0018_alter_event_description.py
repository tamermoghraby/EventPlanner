# Generated by Django 4.0.4 on 2022-06-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanner', '0017_alter_event_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=60),
        ),
    ]