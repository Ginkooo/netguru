# Generated by Django 2.2.4 on 2019-08-07 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
            preserve_default=False,
        ),
    ]
