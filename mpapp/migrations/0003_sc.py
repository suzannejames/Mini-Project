# Generated by Django 4.2.1 on 2023-06-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpapp', '0002_tutor_registration_interview'),
    ]

    operations = [
        migrations.CreateModel(
            name='SC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=7)),
                ('time', models.TimeField()),
                ('note', models.TextField()),
            ],
        ),
    ]
