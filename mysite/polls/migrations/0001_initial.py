# Generated by Django 4.2.5 on 2023-10-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
                ('knowledge', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
