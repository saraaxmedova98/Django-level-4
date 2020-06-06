# Generated by Django 3.0.7 on 2020-06-06 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTask', '0004_car_manufacturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='Fullname')),
                ('image', models.ImageField(upload_to='partials/images', verbose_name='Image')),
                ('gender', models.BinaryField(verbose_name='Gender')),
                ('date_of_birthday', models.DateField(auto_now_add=True, verbose_name='Date of birthday')),
                ('nationality', models.CharField(max_length=50, verbose_name='Nationality')),
                ('info', models.TextField(default='', verbose_name='Info')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('page_count', models.IntegerField(verbose_name='Page count')),
                ('cover_image', models.ImageField(upload_to='partials/images', verbose_name='Cover image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelsTask.Author', verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', verbose_name='Title')),
                ('books', models.ManyToManyField(to='modelsTask.Book', verbose_name='Book')),
            ],
        ),
    ]