# Generated by Django 2.2.3 on 2019-08-09 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190809_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='summary',
            options={'get_latest_by': 'obj_count', 'ordering': ['-pub_date'], 'verbose_name_plural': 'Summaries'},
        ),
    ]
