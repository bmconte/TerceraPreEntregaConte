from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm

def insertar_datos(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        producto_form = ProductoForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if categoria_form.is_valid() and producto_form.is_valid() and cliente_form.is_valid():
            categoria_form.save()
            producto_form.save()
            cliente_form.save()
            return redirect('insertar_datos')
    else:
        categoria_form = CategoriaForm()
        producto_form = ProductoForm()
        cliente_form = ClienteForm()

    return render(request, 'insertar_datos.html', {'categoria_form': categoria_form, 'producto_form': producto_form, 'cliente_form': cliente_form})

def buscar_datos(request):
    if request.method == 'POST':
        # Lógica para buscar datos en la base de datos
        pass
    else:
        # Renderizar la página de búsqueda
        pass
