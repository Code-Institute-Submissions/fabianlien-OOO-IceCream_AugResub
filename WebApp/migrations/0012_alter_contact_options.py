# Generated by Django 3.2.13 on 2022-05-12 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0011_auto_20220512_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['name']},
        ),
    ]
