# Generated by Django 4.0.3 on 2022-03-25 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_rename_caption_post_body_remove_post_date_posted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
