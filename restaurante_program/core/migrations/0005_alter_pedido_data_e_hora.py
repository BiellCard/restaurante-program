# Generated by Django 4.2.4 on 2023-10-03 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_garcom_comida_imagem_alter_pedido_data_e_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_e_hora',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 19, 45, 6, 438602)),
        ),
    ]
