# Generated by Django 2.2.4 on 2019-08-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_comment_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='details',
            field=models.TextField(default=set),
        ),
    ]