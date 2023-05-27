from django.shortcuts import render
from sympy.calculus.util import continuous_domain
import pandas as pd
import numpy as np
from sympy import *
import math

# Create your views here.
def home_page(request):
    return render(request,template_name='home.html')

def menu_page(request):
    return render(request,template_name='menu.html')

def biseccion_page(request):
    if request.method == 'POST':
        x, y, z = symbols('x y z')
        Fun = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tipo_error = int(request.POST.get('tipo_de_tolerancia'))
        num_tol = float(request.POST.get('numero_de_tolerancia'))
        Niter = int(request.POST.get('iteraciones'))
        inia = a
        inib = b
        df=0


        if tipo_error == 1: 
            tipo = "decimales correctos"
            Tol = 0.5*(10**-num_tol)
        elif tipo_error == 2: 
            tipo = "cifras significativas"
            Tol = 5*(10**-num_tol)
        
        Fun = sympify(Fun)
        func = lambda m: Fun.evalf(15, subs = {x: m})
        x_vals, fm, E, iters = [], [], [], []
        fa = func(a)
        fb = func(b)
        
        if fa == 0:
            s = a
            E = 0
            mensaje = str(s) + " es raiz de f(x)"
        
        elif fb == 0:
            s = b
            E = 0
            mensaje = str(s) + " es raiz de f(x)"
            
        elif fa*fb < 0:
            c = 0
            Xm = (a + b)/2                
            fe = func(Xm)
            fm.append(fe)
            x_vals.append(Xm)
            E.append(100)
            iters.append(c)
        
            while E[c] >= Tol and fe!= 0 and c < Niter:
                if fa*fe < 0: 
                    b = Xm              
                    fb = func(b)
                else:
                    a = Xm
                    fa = func(a)
                
                c = c+1
                Xm = (a + b)/2
                fe = func(Xm)
                fm.append(fe)
                x_vals.append(Xm)
                iters.append(c)
                
                if tipo_error == 1: 
                    Error_abs = abs(x_vals[c] - x_vals[c-1])
                    E.append(Error_abs)
                elif tipo_error == 2: 
                    Error_rel = abs((x_vals[c] - x_vals[c-1])/x_vals[c])
                    E.append(Error_rel)
                
            if fe == 0:
                s = Xm
                mensaje = str(s) + " es raiz de f(x)"
            
            elif E[c] < Tol:
                s = Xm
                d = {"Iteraciones": iters, "Xn": x_vals, "f(Xn)": fm, "Error": E}
                df = pd.DataFrame(d)

                mensaje = f"La solución aproximada es: {s}, con una tolerancia = {Tol} ({tipo})"
                
            else:
                s = Xm
                mensaje = "Fracaso en "+ str(Niter)+ " iteraciones "
        
        else:
            mensaje = "El intervalo es inadecuado"

        context={'mensaje':mensaje,'df':df,'fun':Fun,'a':inia,'b':inib,'tipo_error':tipo,'num_tol':num_tol,'niter':Niter}
        return render(request,template_name='1-biseccion.html',context=context)
    
    if request.method == 'GET':
        return render(request,template_name='1-biseccion.html')

def regla_falsa_page(request):
    x, y, z = symbols('x y z')
    if request.method == 'POST':
        Fun = request.POST.get('funcion')
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        tipo_error = int(request.POST.get('tipo_de_tolerancia'))
        num_tol = float(request.POST.get('numero_de_tolerancia'))
        Niter = int(request.POST.get('iteraciones'))
        inia = a
        inib = b
        df=0

        if tipo_error == 1: 
            tipo = "decimales correctos"
            Tol = 0.5*(10**-num_tol)
        elif tipo_error == 2: 
            tipo = "cifras significativas"
            Tol = 5*(10**-num_tol)
        
        Fun = sympify(Fun)
        func = lambda m: Fun.evalf(15, subs = {x: m})
        x_vals, fm, E, iters = [], [], [], []
        fa = func(a)
        fb = func(b)
        
        if fa == 0:
            s = a
            E = 0
            mensaje = str(s) + " es raiz de f(x)"
        
        elif fb == 0:
            s = b
            E = 0
            mensaje = str(s) + " es raiz de f(x)"
            
        elif fa*fb < 0:
            c = 0
            Xm = a - (fa*(b-a))/(fb - fa)         
            fe = func(Xm)
            fm.append(fe)
            x_vals.append(Xm)
            E.append(100)
            iters.append(c)
        
            while E[c] >= Tol and fe!= 0 and c < Niter:
                if fa*fe < 0: 
                    b = Xm              
                    fb = func(b)
                else:
                    a = Xm
                    fa = func(a)
                
                c = c+1
                Xm = a - (fa*(b-a))/(fb - fa)   
                fe = func(Xm)
                fm.append(fe)
                x_vals.append(Xm)
                iters.append(c)
                
                if tipo_error == 1: 
                    Error_abs = abs(x_vals[c] - x_vals[c-1])
                    E.append(Error_abs)
                elif tipo_error == 2: 
                    Error_rel = abs((x_vals[c] - x_vals[c-1])/x_vals[c])
                    E.append(Error_rel)
                
            if fe == 0:
                s = Xm
                mensaje = str(s) + " es raiz de f(x)"
            
            elif E[c] < Tol:
                s = Xm
                d = {"Iteraciones": iters, "Xn": x_vals, "f(Xn)": fm, "Error": E}
                df = pd.DataFrame(d)
                mensaje = f"La solución aproximada es: {s}, con una tolerancia = {Tol} ({tipo})"
           
            else:
                s = Xm
                mensaje = "Fracaso en "+ str(Niter)+ " iteraciones "
            
            context={'mensaje':mensaje,'df':df,'fun':Fun,'a':inia,'b':inib,'tipo_error':tipo,'num_tol':num_tol,'niter':Niter}
            return render(request,template_name='2-regla_falsa.html',context=context)
        
        else:
            mensaje = "El intervalo es inadecuado"

    if request.method == 'GET':
        return render(request,template_name='2-regla_falsa.html')

def punto_fijo_page(request):
    x, y, z = symbols('x y z')
    if request.method == 'POST':
        Fun = request.POST.get('funcion')
        gf = request.POST.get('funcion_g')
        X0 = float(request.POST.get('x0'))
        tipo_error = int(request.POST.get('tipo_de_tolerancia'))
        num_tol = float(request.POST.get('numero_de_tolerancia'))
        Niter = int(request.POST.get('iteraciones'))
        iniX0 = X0
        df=0

        if tipo_error == 1: 
            tipo = "decimales correctos"
            Tol = 0.5*(10**-num_tol)
        elif tipo_error == 2: 
            tipo = "cifras significativas"
            Tol = 5*(10**-num_tol)
        
        Fun = sympify(Fun)
        gf = sympify(gf)
        func = lambda m: Fun.evalf(15, subs = {x: m})
        g = lambda m: gf.evalf(15, subs = {x: m})

        fn, xn, E, iters = [], [], [], []
        x_val = X0
        fe = func(X0)
        c, Error = 0, 100
        fn.append(fe)
        xn.append(X0)
        E.append(Error)
        iters.append(c)
        
        while E[c] >= Tol and fe!=0 and c < Niter:
            c = c+1
            x_val = g(X0)
            fe = func(x_val)
            fn.append(fe)
            xn.append(x_val)
            iters.append(c)
            
            if tipo_error == 1: 
                Error_abs = abs(xn[c] - xn[c-1])
                E.append(Error_abs)
            elif tipo_error == 2: 
                Error_rel = abs((xn[c] - xn[c-1])/xn[c])
                E.append(Error_rel)
        
            X0 = x_val
        
        if fe == 0:
            sol = x_val
            mensaje = str(sol) + " es raiz de f(x)"
            
        elif E[c] < Tol:
            sol = x_val 
            d = {"Iteraciones": iters, "Xn": xn, "f(Xn)": fn, "Error": E}
            df = pd.DataFrame(d)
            mensaje = f"La solución aproximada es: {sol}, con una tolerancia = {Tol} ({tipo})"
        
        else:
            sol = x_val
            mensaje = "Fracaso en "+ str(Niter)+ " iteraciones "
        
        context={'mensaje':mensaje,'df':df,'fun':Fun,'x0':iniX0,'gf':gf,'tipo_error':tipo,'num_tol':num_tol,'niter':Niter}
        return render(request,template_name='3-punto_fijo.html',context=context)

    if request.method == 'GET':
        return render(request,template_name='3-punto_fijo.html')

def newton_page(request):
    x, y, z = symbols('x y z')
    if request.method == 'POST':
        Fun = request.POST.get('funcion')
        X0 = float(request.POST.get('x0'))
        tipo_error = int(request.POST.get('tipo_de_tolerancia'))
        num_tol = float(request.POST.get('numero_de_tolerancia'))
        Niter = int(request.POST.get('iteraciones'))
        iniX0 = X0
        df=0
        
        if tipo_error == 1: 
            tipo = "decimales correctos"
            Tol = 0.5*(10**-num_tol)
        elif tipo_error == 2: 
            tipo = "cifras significativas"
            Tol = 5*(10**-num_tol)

        Fun = sympify(Fun)
        func = lambda a: Fun.evalf(15, subs = {x: a})
        derivative = diff(Fun, x)
        deriv = lambda a: diff(Fun, x).evalf(15, subs = {x: a})

        domf = continuous_domain(Fun, x, S.Reals)
        print(domf)
        if not domf.contains(X0):
            mensaje = f"La función no está definida en x = {X0}. El método falla."
            context = {'mensaje':mensaje,'df':df}
            return render(request,template_name='4-newton.html',context=context)
        
        elif not derivative.subs(x, X0).is_finite:
            mensaje = f"La función no es diferenciable en x = {X0}. El método falla."
            context = {'mensaje':mensaje,'df':df}
            return render(request,template_name='4-newton.html',context=context)
        
        else: 
            fn, x_vals, E, dvs, iters = [], [], [], [], []
            xn = X0
            f, derivada = func(xn), deriv(xn)
            c, Error = 0, 100         
            fn.append(f)
            dvs.append(derivada)
            x_vals.append(xn)
            E.append(Error)
            iters.append(c)
            while (E[c] >= Tol) and (f != 0) and (derivada != 0) and (c < Niter):
                c = c+1
                xn = xn - (f/derivada)
                
                if not domf.contains(xn):
                    mensaje = "La función no está definida en x{c} = {xn}. El método falla."
                    context = {'mensaje':mensaje,'df':df}
                    return render(request,template_name='4-newton.html',context=context)

                elif not derivative.subs(x,xn).is_finite:
                    mensaje = "La función no es diferenciable en x{c} = {xn}. El método falla."
                    context = {'mensaje':mensaje,'df':df}
                    return render(request,template_name='4-newton.html',context=context)
                    
                f, derivada = func(xn), deriv(xn)
                fn.append(f)
                dvs.append(derivada)
                x_vals.append(xn)
                iters.append(c)
            
                if tipo_error == 1: 
                    Error_abs = abs(x_vals[c] - x_vals[c-1])
                    E.append(Error_abs)
                elif tipo_error == 2: 
                    Error_rel = abs((x_vals[c] - x_vals[c-1])/x_vals[c])
                    E.append(Error_rel)
            
            if f == 0:
                s = xn
                mensaje = str(s)+"es raiz de f(x)"
                context = {'mensaje':mensaje,'df':df}
                return render(request,template_name='4-newton.html',context=context)
            
            if derivada == 0:
                s = xn
                mensaje = f"La derivada es 0 en x = {s}. El método falla."
                context = {'mensaje':mensaje,'df':df}
                return render(request,template_name='4-newton.html',context=context)
                
            elif E[c] < Tol:
                s = xn
                d = {"Iteraciones": iters, "Xn": x_vals, "f(Xn)": fn, "f'(Xn)": dvs, "Error": E}
                df = pd.DataFrame(d) 
                mensaje = f"La solución aproximada es: {s}, con una tolerancia = {Tol} ({tipo})"
                context={'mensaje':mensaje,'df':df,'fun':Fun,'x0':iniX0,'tipo_error':tipo,'num_tol':num_tol,'niter':Niter}
                return render(request,template_name='4-newton.html',context=context)
            
            else:
                s = xn
                mensaje = "Fracaso en"+ str(Niter) + "iteraciones"
                context = {'mensaje':mensaje,'df':df}
                return render(request,template_name='4-newton.html',context=context)

    if request.method == 'GET':
        return render(request,template_name='4-newton.html')
    
def raices_multiples_page(request):
    x, y, z = symbols('x y z')
    if request.method == 'POST':
        Fun = request.POST.get('funcion')
        X0 = float(request.POST.get('x0'))
        tipo_error = int(request.POST.get('tipo_de_tolerancia'))
        num_tol = float(request.POST.get('numero_de_tolerancia'))
        Niter = int(request.POST.get('iteraciones'))
        iniX0 = X0
        df=0
        
        if tipo_error == 1: 
            tipo = "decimales correctos"
            Tol = 0.5*(10**-num_tol)
        elif tipo_error == 2: 
            tipo = "cifras significativas"
            Tol = 5*(10**-num_tol)
        
        Fun = sympify(Fun)
        func = lambda a: Fun.evalf(15, subs = {x: a})
        derivative = diff(Fun, x)
        deriv = lambda a: diff(Fun, x).evalf(15, subs = {x: a})
        derivative2 = diff(Fun, x, 2)
        deriv2 = lambda a: diff(Fun, x, 2).evalf(15, subs = {x: a})
        
        domf = continuous_domain(Fun, x, S.Reals)
        if not domf.contains(X0):
            mensaje = f"La función no está definida en x = {X0}. El método falla."
            context = {'mensaje':mensaje,'df':df}
            return render(request,template_name='5-raices_multiples.html',context=context)
            
        elif not derivative.subs(x, X0).is_finite:
            mensaje = f"La función no es diferenciable en x = {X0}. El método falla."
            context = {'mensaje':mensaje,'df':df}
            return render(request,template_name='5-raices_multiples.html',context=context)
        
        elif not derivative2.subs(x, X0).is_finite:
            mensaje = f"La función no tiene segunda derivada en x = {X0}. El método falla."
            context = {'mensaje':mensaje,'df':df}
            return render(request,template_name='5-raices_multiples.html',context=context)
        
        else: 
            fn, x_vals, E, dvs, dvs2, iters = [], [], [], [], [], []
            xn = X0
            f, derivada, derivada2 = func(xn), deriv(xn), deriv2(xn)
            c, Error = 0, 100         
            fn.append(f)
            dvs.append(derivada)
            dvs2.append(derivada2)
            x_vals.append(xn)
            E.append(Error)
            iters.append(c)
            
            while (E[c] >= Tol) and (f != 0) and (derivada**2 - (f*derivada2)) != 0  and (c < Niter):
                c = c + 1
                xn = xn - (f*derivada)/(derivada**2 - (f*derivada2))
                
                if not domf.contains(xn):
                    mensaje = f"La función no está definida en x{c} = {xn}. El método falla."
                    context = {'mensaje':mensaje,'df':df}
                    return render(request,template_name='5-raices_multiples.html',context=context)

                elif not derivative.subs(x,xn).is_finite:
                    mensaje = f"La función no es diferenciable en x{c} = {xn}. El método falla."
                    context = {'mensaje':mensaje,'df':df}
                    return render(request,template_name='5-raices_multiples.html',context=context)
                
                elif not derivative2.subs(x,xn).is_finite:
                    mensaje = f"La función no tiene segunda derivada en x{c} = {xn}. El método falla."
                    context = {'mensaje':mensaje,'df':df}
                    return render(request,template_name='5-raices_multiples.html',context=context)
                
                f, derivada, derivada2 = func(xn), deriv(xn), deriv2(xn)
                fn.append(f)
                dvs.append(derivada)
                dvs2.append(derivada2)
                x_vals.append(xn)
                iters.append(c)
                
                if tipo_error == 1: 
                    Error_abs = abs(x_vals[c] - x_vals[c-1])
                    E.append(Error_abs)
                elif tipo_error == 2: 
                    Error_rel = abs((x_vals[c] - x_vals[c-1])/x_vals[c])
                    E.append(Error_rel)
            
            if f == 0:
                s = xn
                mensaje = str(s)+"es raiz de f(x)"
                context = {'mensaje':mensaje,'df':df}
                return render(request,template_name='5-raices_multiples.html',context=context)
            
            if (derivada**2 - (f*derivada2)) == 0:
                s = xn
                mensaje = "El método falla. El denominador es 0."
                context = {'mensaje':mensaje,'df':df}
                return render(request,template_name='5-raices_multiples.html',context=context)
                
            elif E[c] < Tol: #Vuelve
                s = xn
                d = {"Iteraciones": iters, "Xn": x_vals, "f(Xn)": fn, "f'(Xn)": dvs, "f''(Xn)": dvs2, "Error": E}
                df = pd.DataFrame(d) 
                mensaje = f"La solución aproximada es: {s}, con una tolerancia = {Tol} ({tipo})"
                context={'mensaje':mensaje,'df':df,'fun':Fun,'x0':iniX0,'tipo_error':tipo,'num_tol':num_tol,'niter':Niter}
                return render(request,template_name='5-raices_multiples.html',context=context)
            
            else:
                s = xn
                mensaje = f"Fracaso en {Niter} iteraciones"
                context = {'mensaje':mensaje,'df':df}
                return render(request,template_name='5-raices_multiples.html',context=context)

    if request.method == 'GET':
        return render(request,template_name='5-raices_multiples.html')

def secante_page(request):
    if request.method == 'POST':
        x, y, z = symbols('x y z')
        Fun = request.POST.get('funcion')
        X0 = float(request.POST.get('x0'))
        X1 = float(request.POST.get('x1'))
        tipo_error = int(request.POST.get('tipo_de_tolerancia'))
        num_tol = float(request.POST.get('numero_de_tolerancia'))
        Niter = int(request.POST.get('iteraciones'))
        iniX0 = X0
        iniX1 = X1
        df=0
        
        if tipo_error == 1: 
            tipo = "decimales correctos"
            Tol = 0.5*(10**-num_tol)
        elif tipo_error == 2: 
            tipo = "cifras significativas"
            Tol = 5*(10**-num_tol)
        
        Fun = sympify(Fun)
        func = lambda m: Fun.evalf(15, subs = {x: m})
        
        domf = continuous_domain(Fun, x, S.Reals)
        if not domf.contains(X0):
            mensaje = f"La función no está definida en x = {X0}. El método falla."
            context = {'mensaje':mensaje,'df':df}
            return render(request,template_name='6-secante.html',context=context)
        elif not domf.contains(X1):
            mensaje = f"La función no está definida en x = {X1}. El método falla."
            context = {'mensaje':mensaje,'df':df}
            return render(request,template_name='6-secante.html',context=context)
        
        else: 
            fn, xn, E, iters = [], [], [], []
            f0, f1 = func(X0), func(X1)
            fn.extend([f0,f1])
            xn.extend([X0,X1])
            E.extend([abs(100), abs(X0-X1)])
            iters.extend([0,1])
            
            if f0 == 0:
                mensaje = str(X0)+" es raiz de f(x)"
            
            elif f1 == 0:
                mensaje = str(X1)+" es raiz de f(x)"
            
            else:
                c = 1
                x_val = X1
                while (E[c] >= Tol) and (fn[c] != 0) and (f1-f0 != 0)  and (c < Niter):
                    X1, X0 = xn[c], xn[c-1]
                    f1, f0 = fn[c], fn[c-1]
                    c = c+1
                    x_val = X1 - (f1*(X1-X0))/(f1 - f0)   
                    
                    if not domf.contains(x_val):
                        mensaje = f"La función no está definida en x{c} = {x_val}. El método falla."
                        context = {'mensaje':mensaje,'df':df}
                        return render(request,template_name='6-secante.html',context=context)
                        
                        
                    fe = func(x_val)
                    fn.append(fe)
                    xn.append(x_val)
                    iters.append(c)
        
                    if tipo_error == 1: 
                        Error_abs = abs(xn[c] - xn[c-1])
                        E.append(Error_abs)
                    elif tipo_error == 2: 
                        Error_rel = abs((xn[c] - xn[c-1])/xn[c])
                        E.append(Error_rel)
                
                if fn[c] == 0:
                    s = x_val
                    mensaje = str(s)+"es raiz de f(x)"
                    context = {'mensaje':mensaje,'df':df}
                    return render(request,template_name='6-secante.html',context=context)
                
                if (f1-f0 == 0):
                    mensaje = "El método falla"
                    context = {'mensaje':mensaje,'df':df}
                    return render(request,template_name='6-secante.html',context=context)
                
                elif E[c] < Tol:
                    s = x_val
                    d = {"Iteraciones": iters, "Xn": xn, "f(Xn)": fn, "Error": E}
                    df = pd.DataFrame(d) 
                    mensaje = f"La solución aproximada es: {s}, con una tolerancia = {Tol} ({tipo})"
                    context={'mensaje':mensaje,'df':df,'fun':Fun,'x0':iniX0,'x1':iniX1,'tipo_error':tipo,'num_tol':num_tol,'niter':Niter}
                    return render(request,template_name='4-newton.html',context=context)
                
                else:
                    s = x_val
                    mensaje = f"Fracaso en {Niter} iteraciones "
                    context = {'mensaje':mensaje,'df':df}
                    return render(request,template_name='6-secante.html',context=context)

    if request.method == 'GET':
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