# Generated by Django 2.0 on 2018-01-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.CharField(max_length=4000)),
                ('note_title', models.CharField(max_length=200)),
            ],
        ),
    ]
