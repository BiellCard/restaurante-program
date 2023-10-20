# Generated by Django 4.2.4 on 2023-09-28 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pedido_comidas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='comidas',
        ),
        migrations.CreateModel(
            name='comidas_pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('comida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comida')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
            ],
        ),
    ]
