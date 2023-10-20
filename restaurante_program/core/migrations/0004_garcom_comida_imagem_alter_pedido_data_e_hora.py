# Generated by Django 4.2.4 on 2023-10-02 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_pedido_comidas_comidas_pedidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garcom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comida',
            name='imagem',
            field=models.ImageField(default=None, upload_to='imagens/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_e_hora',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 2, 19, 31, 8, 815963)),
        ),
    ]
