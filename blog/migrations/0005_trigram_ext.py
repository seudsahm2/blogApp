# Generated by Django 5.1.1 on 2024-09-12 07:49
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        TrigramExtension()
    ]
