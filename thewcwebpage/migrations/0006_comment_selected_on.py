# Generated by Django 4.2.5 on 2023-09-26 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thewcwebpage', '0005_comment_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='selected_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
