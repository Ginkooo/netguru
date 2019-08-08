# Generated by Django 2.2.4 on 2019-08-08 21:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('movies', '0001_initial'), ('movies', '0002_comment_movie'), ('movies', '0003_movie_details'), ('movies', '0004_movie_year'), ('movies', '0005_auto_20190807_1930'), ('movies', '0006_comment_added_at'), ('movies', '0007_auto_20190808_1949'), ('movies', '0008_movie_year')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField(default=set)),
                ('year', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('movie', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('added_at', models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
