# Generated by Django 3.2.13 on 2022-07-24 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220721_0121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created_on',)},
        ),
    ]
