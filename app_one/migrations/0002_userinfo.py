# Generated by Django 2.2 on 2020-01-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128, unique=True)),
            ],
        ),
    ]
