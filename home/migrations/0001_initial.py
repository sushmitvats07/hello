# Generated by Django 4.1.4 on 2022-12-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=600)),
                ('img_url', models.CharField(max_length=600)),
                ('link', models.CharField(max_length=600)),
            ],
        ),
    ]
