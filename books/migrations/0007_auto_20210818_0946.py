# Generated by Django 3.2.6 on 2021-08-18 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]