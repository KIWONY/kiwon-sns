# Generated by Django 4.0.6 on 2022-07-24 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_remove_article_hashtag_article_hashtags_hashtag'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='hashtag',
            table='hashtag',
        ),
    ]