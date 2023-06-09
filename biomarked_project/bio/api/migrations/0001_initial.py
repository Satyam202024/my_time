# Generated by Django 4.2.2 on 2023-06-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biomarked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('1', 'Amazon'), ('2', 'Flipkart')], max_length=50)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('link', models.CharField(blank=True, max_length=50, null=True)),
                ('i_frame', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
