# Generated by Django 4.0.4 on 2022-06-02 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventPlanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=30),
        ),
    ]
