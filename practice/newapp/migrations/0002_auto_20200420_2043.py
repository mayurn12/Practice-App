# Generated by Django 3.0.4 on 2020-04-20 15:13

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelform',
            name='mobile',
        ),
        migrations.AddField(
            model_name='modelform',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
