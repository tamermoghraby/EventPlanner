# Generated by Django 4.0.4 on 2022-06-02 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanner', '0003_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.TimeField(),
        ),
    ]
