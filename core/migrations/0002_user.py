# Generated by Django 3.2.9 on 2022-01-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('fullname', models.TextField()),
            ],
        ),
    ]
