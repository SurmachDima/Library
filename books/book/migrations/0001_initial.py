# Generated by Django 3.2.6 on 2021-08-20 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название книги')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
                ('year_published', models.DateField(max_length=4, verbose_name='Год публикации')),
                ('pages', models.CharField(max_length=6, verbose_name='Количество страниц')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.author', verbose_name='Автор')),
                ('genre', models.ManyToManyField(to='book.Genre', verbose_name='Жанр')),
            ],
        ),
    ]