# Generated by Django 4.2.2 on 2023-07-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_billmember_position_billmember_unique_position'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='billmember',
            name='unique_position',
        ),
        migrations.AlterField(
            model_name='billmember',
            name='position',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
    ]
