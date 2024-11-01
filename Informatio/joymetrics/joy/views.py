from django.shortcuts import render

# Create your views here.
def Inicio(request):
    label = ['Economia', 'Familia', 'Generocidad', 'Salud', 'corrupccion', 'libertad']
    data = [1, 0.8, 0.4, 0.5, 0.2, 0.5]

    return render(request, 'inicio.html', {'label': label, 'data': data,})

def graficos_view(request):
    return render(request, 'graficos.html')

def Grafico2(request):
    label = ['Economia', 'Familia', 'Generocidad', 'Salud', 'corrupccion', 'libertad']
    data = [1.5, 1, 0.04, 1.0, 0.6, 0.9]

    return render(request, 'grafico.html', {'label': label, 'data': data,})

def log(request):
    return render(request, 'log.html')

def registro(request):
    return render(request, 'registro.html')

def main(request):
    return render(request, 'main.html')

def contacto(request):
    return render(request, 'contacto.html')


def quienes(request):
    return render(request, 'quienes.html')