# advocacia/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Processo
from .forms import ClienteForm, ProcessoForm

# Views para Clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'advocacia/lista_clientes.html', {'clientes': clientes})

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'advocacia/form_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'advocacia/form_cliente.html', {'form': form})

def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'advocacia/excluir_cliente.html', {'cliente': cliente})

# Views para Processos
def lista_processos(request):
    processos = Processo.objects.all()
    return render(request, 'advocacia/lista_processos.html', {'processos': processos})

def adicionar_processo(request):
    if request.method == 'POST':
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_processos')
    else:
        form = ProcessoForm()
    return render(request, 'advocacia/form_processo.html', {'form': form})

def editar_processo(request, pk):
    processo = get_object_or_404(Processo, pk=pk)
    if request.method == 'POST':
        form = ProcessoForm(request.POST, instance=processo)
        if form.is_valid():
            form.save()
            return redirect('lista_processos')
    else:
        form = ProcessoForm(instance=processo)
    return render(request, 'advocacia/form_processo.html', {'form': form})

def excluir_processo(request, pk):
    processo = get_object_or_404(Processo, pk=pk)
    if request.method == 'POST':
        processo.delete()
        return redirect('lista_processos')
    return render(request, 'advocacia/excluir_processo.html', {'processo': processo})

def home(request):
    return redirect('lista_clientes')