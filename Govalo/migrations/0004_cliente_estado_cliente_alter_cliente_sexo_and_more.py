# Generated by Django 4.1.2 on 2022-11-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Govalo', '0003_gyo_estado_de_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado_cliente',
            field=models.CharField(choices=[('SI', 'Activo'), ('NO', 'Inactivo')], default='SI', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gyo',
            name='Estado_de_Pedido',
            field=models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aprobado')], max_length=1),
        ),
        migrations.AlterField(
            model_name='morosidad',
            name='cantidad_de_cuotas_impagas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='morosidad',
            name='cantidad_de_cuotas_pagas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='suscripcion',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]