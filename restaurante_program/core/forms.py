from django import forms
from .models import *
from django.forms import ModelForm

class Form_Categoria(forms.Form):
    class Meta:
        model = Categoria
        fields = '__all__'

class Form_Comida(ModelForm):
    class Meta:
        model = Comida
        fields = '__all__'

class Form_Pedido(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class Form_comida_pedidos(ModelForm):
    class Meta:
        model = comidas_pedidos
        fields = '__all__'