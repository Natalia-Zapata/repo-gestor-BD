from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto  = {}

    return render(request, 'inicio.html', contexto)

def list_productos(request):
    productos=['portatil lenovo',' galaxiA35','Rolex']
    contexto={'listado':productos}


    return render(request, 'list_productos.html', contexto)

