# Generated by Django 4.2.7 on 2023-12-12 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_studentmodel_slug_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='positive_integer_field',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
