# Generated by Django 4.1 on 2022-09-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchListAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.TextField()),
                ('title', models.TextField()),
                ('rating', models.FloatField()),
                ('release_date', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]
