# Generated by Django 4.0.3 on 2022-03-24 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_flan_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flan',
            name='price',
        ),
    ]
