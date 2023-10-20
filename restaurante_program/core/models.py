from django.db import models
from datetime import datetime

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Comida(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="imagens/")
    
    def __str__(self):
        return self.nome

class Garcom(models.Model):
    nome = models.CharField(max_length=50)

class Pedido(models.Model):
    data_e_hora = models.DateTimeField(default=datetime.now())
    ativo = models.BooleanField(default=0)
    
    def __str__(self):
        return f'Pedido {self.id}'

class comidas_pedidos(models.Model):
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
