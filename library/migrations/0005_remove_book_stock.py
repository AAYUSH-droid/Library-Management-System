# Generated by Django 4.1.5 on 2023-08-08 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='stock',
        ),
    ]
