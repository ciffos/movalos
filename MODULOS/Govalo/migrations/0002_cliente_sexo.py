# Generated by Django 4.1.2 on 2022-10-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Govalo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], default='m', max_length=1),
        ),
    ]