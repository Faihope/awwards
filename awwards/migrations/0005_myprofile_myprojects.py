# Generated by Django 3.2.5 on 2021-07-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0004_auto_20210722_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Myprojects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
        ),
    ]
