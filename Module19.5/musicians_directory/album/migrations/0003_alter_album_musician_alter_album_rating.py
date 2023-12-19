# Generated by Django 4.2.7 on 2023-12-12 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
        ('album', '0002_album_musician_alter_album_album_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='musician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician'),
        ),
        migrations.AlterField(
            model_name='album',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
    ]