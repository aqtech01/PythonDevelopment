# Generated by Django 5.0.1 on 2024-01-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=18)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
