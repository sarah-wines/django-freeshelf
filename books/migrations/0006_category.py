# Generated by Django 3.2.6 on 2021-08-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_author_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]