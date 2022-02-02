# Generated by Django 3.1.6 on 2022-01-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestry_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rejestr',
            name='zakres_lista',
        ),
        migrations.AddField(
            model_name='rejestr',
            name='atrybuty_liczba',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rejestr',
            name='obiekty_liczba',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
    ]
