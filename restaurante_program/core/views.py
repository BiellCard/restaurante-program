from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def deslogar(request):
    logout(request)
    return redirect(logar)

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect(logar)
    else:
        form = AuthenticationForm()
    return render(request, 'logar.html', {'form': form})

def cadastrar_comida(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = Form_Comida(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Form_Comida()
    return render(request, 'cadastrar_comida.html', {'categorias': categorias, 'form': form})

def pagina_inicial(request):
    comidas = Comida.objects.all()
    if request.method == 'POST':
        form = Form_Pedido(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form_Pedido()

    return render(request, 'pagina_inicial.html', {'comidas': comidas, 'form': form})

def listar_pedido(request):
    pedidos_ativos = Pedido.objects.filter(ativo=1)
    pedidos_inativos = Pedido.objects.filter(ativo=0)

    return render(request, 'listar_pedido.html', {'pedidos_ativos': pedidos_ativos, 'pedidos_inativos': pedidos_inativos})

def cadastrar_categoria(request):
    form = Form_Categoria()
    if request.method == 'POST':
        # Abrindo a carta
        nome_categoria = request.POST['nome']

        # Salvando no banco de dados
        Categoria.objects.create(nome=nome_categoria)

    return render(request, 'cadastro_categoria.html', {'form': form})

def editar_categoria(request, id_categoria):
    categoria_puxada = Categoria.objects.get(id=id_categoria)

    if request.method == 'POST':
        categoria_puxada.nome = request.POST['nome.categoria']
        categoria_puxada.save()
        return redirect(editar_categoria)
    
    return render(request, 'editar_categoria.html', {'categoria': categoria_puxada})

def editar_comida(request, id_comida):
    categorias = Categoria.objects.all()
    comida = Comida.objects.get(id=id_comida)
    if request.method == "POST":
        comida.nome = request.POST['nome_comida']
        comida.descricao = request.POST['descricao_comida']
        comida.estoque = request.POST['estoque']
        comida.preco = request.POST['preco']
        comida.categoria = Categoria.objects.get(id=request.POST['id_categoria'])

        comida.save()

    return render(request, 'editar_comida.html', {'comida': comida, 'categorias': categorias})

def fechar_pedido(request, id_pedido):
    pedidos = Pedido.objects.get(id=id_pedido)
    if pedidos.ativo==0:
        pedidos.ativo=1
    else:
        pedidos.ativo=0

    pedidos.save()
    return redirect(listar_pedido)

def comidanpedido(request):
    form = Form_comida_pedidos()
    if request.method == 'POST':

        comida = request.POST['comida']
        pedido = request.POST['pedido']
        quantidade = request.POST['quantidade']

        comidas_pedidos.objects.create(comida=comida, pedido=pedido, quantidade=quantidade)

    return render(request, 'comidanpedido.html', {'form': form})

def cadastrar_garcom(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'cadastrar_garcom.html', {'form': form})