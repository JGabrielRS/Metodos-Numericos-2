def f(x):
    return x**2 + 3*x + 5

#derivadas foward
def derivada_foward(x, delta):
    return (f(x+delta)-f(x))/delta

def derivada_foward_erroO2(x, delta):
    return (-f(x+2*delta)+4*(f(x+delta))-3*(f(x)))/(2*delta)

def derivada_foward_erroO3(x, delta):
    return (2*f(x+3*delta)-9*f(x+2*delta)+18*f(x+delta)-11*f(x))/(6*delta)

def derivada_foward_segundaOrdem(x, delta):
    return (f(x+2*delta)-2*f(x+delta)+f(x))/(delta ** 2)

def derivada_foward_terceiraOrdem(x,delta):
    return (f(x+3*delta)-3*f(x+2*delta)+3*f(x+delta)-f(x))/delta**3

#derivadas backward
def derivada_backward(x, delta):
    return (f(x)-f(x-delta))/delta

def derivada_backward_erroO2(x, delta):
    return (3*f(x)-4*f(x-delta)+f(x-2*delta))/(2*delta)

def derivada_backward_erroO3(x, delta):
    return (11*f(x)-18*f(x-delta)+9*f(x-2*delta)-2*f(x-3*delta))/(6*delta)

def derivada_backward_segundaOrdem(x, delta):
    return (f(x)-2*f(x-delta)+f(x-2*delta))/(delta**2)

#derivadas central
def derivada_central_erroO2(x, delta):
    return (f(x+delta)-f(x-delta))/(2*delta)

def derivada_central_erroO3(x, delta):
    return (-f(x+2*delta)+8*f(x+delta)-8*f(x-delta)+f(x-2*delta))/(12*delta)

def derivada_central_segundaOrdem(x, delta):
    return (f(x+2*delta)-2*f(x)+f(x-2*delta))/(4*(delta**2))