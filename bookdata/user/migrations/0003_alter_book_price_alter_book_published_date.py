# Generated by Django 4.0.6 on 2023-06-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_category_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(auto_created=True),
        ),
    ]
