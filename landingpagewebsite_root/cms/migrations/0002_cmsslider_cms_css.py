# Generated by Django 4.2.2 on 2023-06-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
    ]
