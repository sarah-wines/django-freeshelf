# Generated by Django 3.2.4 on 2021-08-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=2000)),
                ('website', models.URLField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
