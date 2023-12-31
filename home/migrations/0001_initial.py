# Generated by Django 4.2.7 on 2023-11-08 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('middle_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('age', models.IntegerField(default=18)),
                ('father_name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('mobile_no', models.CharField(default='', max_length=15)),
                ('gender', models.CharField(default='', max_length=20)),
                ('hobbies', models.CharField(default='', max_length=200)),
                ('country_name', models.CharField(default='', max_length=200)),
                ('about', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
