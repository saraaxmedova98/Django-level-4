# Generated by Django 3.0.7 on 2020-06-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTask', '0002_auto_20200604_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True)),
                ('production_date', models.DateField(auto_now_add=True)),
                ('is_new', models.BinaryField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
