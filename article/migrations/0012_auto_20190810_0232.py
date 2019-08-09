# Generated by Django 2.2.4 on 2019-08-09 17:32

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_merge_20190810_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='stars_count',
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='article'),
        ),
    ]