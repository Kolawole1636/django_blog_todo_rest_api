# Generated by Django 3.2.13 on 2022-07-09 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='img',
        ),
    ]
