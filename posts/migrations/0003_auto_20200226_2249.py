# Generated by Django 3.0.3 on 2020-02-26 16:49

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200226_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(max_length=300, null=True, validators=[posts.models.Posts.min_length_check]),
        ),
    ]
