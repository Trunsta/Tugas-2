# Generated by Django 4.1 on 2022-09-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(),
        ),
    ]
