# Generated by Django 3.0.5 on 2021-05-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency_Details',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=200)),
                ('change', models.CharField(max_length=200)),
                ('percent_change', models.TextField(max_length=150)),
            ],
        ),
    ]
