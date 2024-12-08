# Generated by Django 5.1.3 on 2024-12-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_addlibrarymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('price', models.IntegerField(max_length=255)),
                ('quantity', models.IntegerField(max_length=255)),
            ],
        ),
    ]