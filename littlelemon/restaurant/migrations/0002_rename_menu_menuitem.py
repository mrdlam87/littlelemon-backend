# Generated by Django 4.2.3 on 2023-07-27 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Menu", new_name="MenuItem",),
    ]
