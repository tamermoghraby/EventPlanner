# Generated by Django 4.0.4 on 2022-06-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanner', '0009_alter_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
