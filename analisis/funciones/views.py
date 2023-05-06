from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,template_name='home.html')

def menu_page(request):
    return render(request,template_name='menu.html')

def biseccion_page(request):
    return render(request,template_name='1-biseccion.html')

def regla_falsa_page(request):
    return render(request,template_name='2-regla_falsa.html')

def punto_fijo_page(request):
    return render(request,template_name='3-punto_fijo.html')

def newton_page(request):
    return render(request,template_name='4-newton.html')

def raices_multiples_page(request):
    return render(request,template_name='5-raices_multiples.html')

def secante_page(request):
    return render(request,template_name='6-secante.html')

def jacobi_page(request):
    return render(request,template_name='7-jacobi.html')

def gauss_seidel_page(request):
    return render(request,template_name='8-gauss_seidel.html')

def SOR_page(request):
    return render(request,template_name='9-SOR.html')

def vandermonde_page(request):
    return render(request,template_name='10-vandermonde.html')

def newton_diferencias_divididas_page(request):
    return render(request,template_name='11-newton_diferencias_divididas.html')

def lagrange_page(request):
    return render(request,template_name='12-lagrange.html')

def spline_page(request):
    return render(request,template_name='13-spline.html')

def grafica_page(request):
    return render(request,template_name='grafica.html')