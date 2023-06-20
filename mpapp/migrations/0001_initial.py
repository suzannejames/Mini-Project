# Generated by Django 4.2.1 on 2023-06-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Langs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('name1', models.CharField(max_length=250)),
                ('desc', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Languages_offered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lang', models.CharField(max_length=250)),
                ('prof', models.CharField(max_length=250)),
                ('rating', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='tutor_Registration',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lang', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_Registration',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lang', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
            ],
        ),
    ]