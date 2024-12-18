# Generated by Django 5.1.3 on 2024-12-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_addbookmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckInModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookId', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('availability', models.CharField(max_length=255)),
                ('rent', models.CharField(max_length=255)),
                ('libraryname', models.CharField(max_length=255)),
                ('userId', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('startDate', models.CharField(max_length=255)),
                ('endDate', models.CharField(max_length=255)),
                ('fine', models.CharField(max_length=255)),
                ('depositedIn', models.CharField(max_length=255)),
                ('shelve', models.CharField(max_length=255)),
            ],
        ),
    ]
