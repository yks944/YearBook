# Generated by Django 2.2.12 on 2020-07-09 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('year_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=20, unique=True)),
                ('enroll', models.CharField(default=None, max_length=20)),
                ('year', models.CharField(default='2020', max_length=4)),
                ('branch', models.CharField(default='', max_length=10)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.CharField(default='', max_length=10)),
                ('address', models.TextField()),
            ],
        ),
    ]
