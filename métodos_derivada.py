def f(x):
    return x**2 + 3*x + 5

def derivada_foward(x, delta):
    return (f(x + delta) - f(x))/delta

def derivada_foward_segundaOrdem(x, delta):
    return (f(x+2*delta) - 2*f(x+delta) + f(x))/(delta ** 2)

def derivada_backward(x, delta):
    return (f(x) - f(x - delta))/delta

def derivada_backward_segundaOrdem(x, delta):
    return (f(x) - 2*f(x-delta) + f(x-2*delta))/(delta ** 2)

def derivada_central(x, delta):
    return (f(x + delta) - f(x - delta))/(2*delta)

def derivada_central_segundaOrdem(x, delta):
    return (f(x+2*delta)-2*f(x)+f(x-2*delta))/(4*(delta**2))

def printar(x, delta):
    print( 26 * '=')
    print("Derivadas de primera ordem")
    print( 26 * '=')
    print("Derivada Foward: ", end = "")
    print(derivada_foward(x,delta))
    print("Derivada Backward: ", end = "")
    print(derivada_backward(x,delta))
    print("Derivada Central: ", end = "")
    print(derivada_central(x,delta))
    print( 26 * '=')
    print("Derivadas de segunda ordem")
    print( 26 * '=')
    print("Derivada Foward: ", end = "")
    print(derivada_foward_segundaOrdem(x,delta))
    print("Derivada Backward: ", end = "")
    print(derivada_backward_segundaOrdem(x,delta))
    print("Derivada Central: ", end = "")
    print(derivada_central_segundaOrdem(x,delta))

x = float(input("Digite o x para ser calculado a derivada na função x² + 3x + 5: "))
delta = float(input("Digite o delta de x para o calculo da derivada: "))

printar(x, delta)